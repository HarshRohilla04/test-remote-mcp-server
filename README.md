How to Use This MCP Server

This repository contains two example MCP servers:

Local MCP Server: main_local_server.py

Remote MCP Server: main_remote_server.py (used for cloud or proxy deployment)

The following guide explains how to run, test, and connect these servers.

1. Run the Server Locally
Start the local MCP server
uv run fastmcp run main_local_server.py

Test the server using the FastMCP developer interface
uv run fastmcp dev main_local_server.py


After running this command:

A browser link will appear — open it

Change the transport type to STDIO

In the configuration panel, ensure the token key is present (add it manually if required)

2. Run the Server Remotely (Proxy / Cloud Deployment)
Option A — Run the remote server with HTTP transport
fastmcp run main_remote_server.py --transport http --host 0.0.0.0 --port 8000

Option B — Using uv
uv run main_remote_server.py

Test the remote server
uv run fastmcp dev main_remote_server.py


Then:

Open the browser link

Set transport type to HTTP

Add the token key in the configuration if not already present

Using a Proxy Server

If your MCP server is deployed on a cloud platform (for example, fastmcp.cloud), you can connect through a local proxy:

uv run fastmcp run local_proxy_server.py


Note: The proxy server works only when the MCP server is hosted on the cloud.

3. Connect the MCP Server to Claude Desktop

To register your MCP server with Claude Desktop:

uv run fastmcp install claude-desktop <file_name.py>


This command works for both the local server and the cloud/proxy server.

If Claude Desktop Cannot Connect

If Claude Desktop displays an error such as "cannot connect to your server," it may be unable to locate your uv installation.

To fix this:

Run the following in Command Prompt:

where uv


Copy the full path displayed

Open Claude Desktop → Settings → Developer → Edit Config File

Open the config file in VS Code

Add the UV path to the configuration

Close Claude Desktop from Task Manager and reopen it

This resolves the path detection issue.
