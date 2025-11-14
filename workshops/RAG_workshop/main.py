
"""
Personal Knowledge Base RAG System - Workshop Boilerplate
A simple RAG implementation for querying your personal documents.
"""

import os
from pathlib import Path
from typing import List, Dict

import chromadb
from chromadb.config import Settings
from openai import OpenAI

API_KEY = os.getenv("API_KEY", "your-api-key-here")
DOCS_FOLDER = "./my_documents"
CHROMA_DB_PATH = "./chroma_db"

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=API_KEY,
)

chroma_client = chromadb.PersistentClient(path=CHROMA_DB_PATH)


def load_documents(folder_path: str) -> List[Dict[str, str]]:
    """
    Load documents from a folder.
    Supports: .txt, .md files (easily extensible to .pdf, .docx)
    
    Returns: List of dicts with 'content', 'filename', and 'source' keys
    """
    documents = []
    folder = Path(folder_path)
    
    if not folder.exists():
        print(f"Creating documents folder: {folder_path}")
        folder.mkdir(parents=True, exist_ok=True)
        return documents
    
    for file_path in folder.glob("**/*"):
        if file_path.is_file() and file_path.suffix in ['.txt', '.md']:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    documents.append({
                        'content': content,
                        'filename': file_path.name,
                        'source': str(file_path)
                    })
                    print(f"Loaded: {file_path.name}")
            except Exception as e:
                print(f"Error loading {file_path.name}: {e}")
    
    return documents


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """
    Split text into overlapping chunks.
    
    Args:
        text: The text to chunk
        chunk_size: Maximum characters per chunk
        overlap: Characters to overlap between chunks
    """
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        
        if end < len(text):
            last_period = chunk.rfind('.')
            last_newline = chunk.rfind('\n')
            break_point = max(last_period, last_newline)
            
            if break_point > chunk_size * 0.5:
                chunk = chunk[:break_point + 1]
                end = start + break_point + 1
        
        chunks.append(chunk.strip())
        start = end - overlap
    
    return [c for c in chunks if c]


def create_or_get_collection(collection_name: str = "knowledge_base"):
    """
    Create or retrieve a ChromaDB collection.
    """
    try:
        collection = chroma_client.get_collection(name=collection_name)
        print(f"Found existing collection: {collection_name}")
    except:
        collection = chroma_client.create_collection(
            name=collection_name,
            metadata={"description": "Personal knowledge base"}
        )
        print(f"Created new collection: {collection_name}")
    
    return collection


def index_documents(documents: List[Dict[str, str]], collection):
    """
    Chunk and index documents into the vector database.
    """
    all_chunks = []
    all_metadatas = []
    all_ids = []
    
    chunk_id = 0
    
    for doc in documents:
        chunks = chunk_text(doc['content'])
        
        for i, chunk in enumerate(chunks):
            all_chunks.append(chunk)
            all_metadatas.append({
                'filename': doc['filename'],
                'source': doc['source'],
                'chunk_index': i
            })
            all_ids.append(f"doc_{chunk_id}")
            chunk_id += 1
    
    if all_chunks:
        print(f"\nIndexing {len(all_chunks)} chunks...")
        collection.add(
            documents=all_chunks,
            metadatas=all_metadatas,
            ids=all_ids
        )
        print("✓ Indexing complete!")
    else:
        print("No documents to index.")


def search_knowledge_base(query: str, collection, n_results: int = 3) -> List[Dict]:
    """
    Search the knowledge base for relevant chunks.
    
    Returns: List of relevant document chunks with metadata
    """
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    
    retrieved_chunks = []
    if results['documents'][0]:
        for i, doc in enumerate(results['documents'][0]):
            retrieved_chunks.append({
                'content': doc,
                'metadata': results['metadatas'][0][i],
                'distance': results['distances'][0][i] if 'distances' in results else None
            })
    
    return retrieved_chunks


def generate_answer(query: str, context_chunks: List[Dict]) -> str:
    """
    Generate an answer using retrieved context and GitHub Copilot models.
    """
    context = "\n\n".join([
        f"[From {chunk['metadata']['filename']}]\n{chunk['content']}"
        for chunk in context_chunks
    ])
    
    prompt = f"""Based on the following context from my personal documents, please answer the question.
If the answer is not in the context, say "I don't have information about that in your documents."

Context:
{context}

Question: {query}

Answer:"""
    
    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context from the user's personal documents."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    return response.choices[0].message.content


def main():
    """
    Main workflow for the RAG system.
    """
    print("=== Personal Knowledge Base RAG System ===\n")
    
    # Step 1: Load documents
    print(f"Loading documents from: {DOCS_FOLDER}")
    documents = load_documents(DOCS_FOLDER)
    print(f"Loaded {len(documents)} documents\n")
    
    if not documents:
        print("⚠️  No documents found. Please add .txt or .md files to the documents folder.")
        print(f"   Create some documents in: {DOCS_FOLDER}")
        return
    
    # Step 2: Create/get collection
    collection = create_or_get_collection()
    
    # Step 3: Index documents (only if collection is empty)
    if collection.count() == 0:
        index_documents(documents, collection)
    else:
        print(f"Collection already has {collection.count()} chunks indexed.")
        reindex = input("Re-index documents? (y/n): ").lower()
        if reindex == 'y':
            chroma_client.delete_collection(name="knowledge_base")
            collection = create_or_get_collection()
            index_documents(documents, collection)
    
    # Step 4: Interactive query loop
    print("\n" + "="*50)
    print("Ready to answer questions! (Type 'quit' to exit)")
    print("="*50 + "\n")
    
    while True:
        query = input("\n🔍 Your question: ").strip()
        
        if query.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not query:
            continue
        
        print("\n📚 Searching knowledge base...")
        # TODO: search the knowledge base for relevant chunks
        relevant_chunks = search_knowledge_base(query, collection, n_results=3)

        if not relevant_chunks:
            print("No relevant information found.")
            continue
        
        print("\n📄 Found relevant information in:")
        for chunk in relevant_chunks:
            print(f"  - {chunk['metadata']['filename']}")
        
        print("\n💡 Generating answer...")
        answer = generate_answer(query, relevant_chunks)
        print(f"\n{answer}")


if __name__ == "__main__":
    if API_KEY == "your-api-key-here":
        print("⚠️  Please set your API_KEY environment variable.")
        print("\n   export API_KEY='your-api-key-here'")
    else:
        main()