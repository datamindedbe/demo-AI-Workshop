from mcp.server.fastmcp import FastMCP
from typing import Any

mcp = FastMCP("my_super_server")

@mcp.tool()
def my_super_tool(*args, **kwargs) -> Any:
    """
    Describe what the tool does. The function signature is passed to the LLM
    A good description helps in using the tool well.

    Args:
        args: The more thorough the signature, the better
        kwatgs: The more thorough the signature, the better
    
    Returns:
        The more thorough the signature, the better
    """

    
# @mcp.resource("")
# def my_super_resource() -> Any:
#     """
#     Describe what the resource does.
#     """

# @mcp.prompt(title="")
# def my_super_prompt() -> Any:
#     """
#     Describe what the prompt does.
#     """


if __name__ == "__main__":
    mcp.run() # default to transport=stdio, set transport=sse for remote MCP servers