# MCP Workshop

This is the practical part of the MCP workshop. You will learn both how to connect your vscode environment to community MCP servers and how to build your own.

## Prerequisites:
If you are using the dev container, everything should be setup for you.
If not, you will need the following:
- node & npm
- python & uv
- python's fastmcp sdk

## Using MCP Servers

### Connect to npx filesystem MCP Server

If you're using the dev container, the filesystem MCP server is already pre-built for you. All you need to do is to enable the use of the MCP server and its corresponding tools.
![MCP Tools in vscode](images/enable_tools.png)
If you're not using the dev container, add a `.vscode/mcp.json` with the following content:
```json
{
  "servers": {
    "filesystem": {
      "type": "stdio",
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "path to Folder" // Replace the line with your project 
      ]
    }
  }
}
```
You will then have a **start** option appear just above your mcp server name (here, `filesystem`)

### Connect to Atlassian Rovo MCP Server

You can find the Atlassian MCP Server in the vscode extension marketplace, or other ways to install the Atlassian MCP [in the docs](https://support.atlassian.com/atlassian-rovo-mcp-server/docs/setting-up-ides/).

<img src="images/atlassian_in_marketplace.png" alt="Atlassian MCP" width="400"/>

From there, after following the authentication flow, you should have the new Atlassian server and its tools available.

<img src="images/atlassian_mcp_tools.png" alt="Atlassian MCP Tools" width="400"/>

### Hackaway!

There are many places where you can find MCP servers to connect to, here are a few examples:
- MCP can be installed as a VSCode extension, simply look for the **@mcp** filter
- ![MCP as vscode extentions](images/mcp_as_vscode_extensions.png)
- [Github](https://github.com/modelcontextprotocol/servers) is a great source to find a bunch of community MCP servers
- [Smithery ai](https://smithery.ai) also has quite a few of them:
- Docker has now has a tab to quickly install MCP servers on some servers. Currently supports Claude Desktop, Cursor and Gemini CLI (don't see it? Update your docker desktop version)
![Docker MCP Servers](images/docker_desktop.png)

## Building MCP Servers

### Create a tool

The `main.py` is a boilerplate to kick start you in building your own MCP server. Add your tool there

### Run MCP Inspector locally

MCP Inspector gives you a nice, interactive view where you can easily test your MCP server.
You can run it with `uv run mcp dev main.py` then open the link (if it does not open automatically).

![Starting MCP Inspector](images/start_mcp_inspector.png)
![MCP Inspector view](images/mcp_inspector_view.png)

### Connect your MCP Server to your local IDE

Create a folder `.vscode` and a file `.vscode/mcp.json`
Insert the following:
```json
{
    "servers": {
        "demo_mcp": {
        "type": "stdio",
        "command": "uv",
        "args": [
            "--directory",
            "/workspaces/MCP_Workshop", // Adapt this part if you're not using the dev container
            "run",
            "main.py"
            ]
        }
    }
}
```

### Hackaway!

You now have all the _tools_ (😉) to build your own MCP server. 
Try to create more tools, resources and prompts. Inspect and debug them using the MCP Inspector utility.
Remember that you will always need to restart the connection between the client and the server for a new protocol exchange to discover new tools/resources/prompts.