import sqlite3


def init_db():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            service TEXT,
            username TEXT,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()


def add_password(service, username, password):
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO passwords (service, username, password) VALUES (?, ?, ?)',
                   (service, username, password))
    conn.commit()
    conn.close()


def get_passwords():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('SELECT service, username, password FROM passwords')
    results = cursor.fetchall()
    conn.close()
    return results


def main():
    init_db()
    
    while True:
        print("\nPassword Manager")
        print("1. Add password")
        print("2. View passwords")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            service = input("Service: ")
            username = input("Username: ")
            password = input("Password: ")
            add_password(service, username, password)
            print("Password added!")
        elif choice == "2":
            passwords = get_passwords()
            for service, username, password in passwords:
                print(f"{service}: {username} - {password}")
        elif choice == "3":
            break


if __name__ == "__main__":
    main()
