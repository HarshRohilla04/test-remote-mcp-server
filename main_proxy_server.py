from fastmcp import FastMCP

mcp = FastMCP.as_proxy("https://test1-remote-mcp-server.fastmcp.app/mcp", name = "Test Proxy Server")

if __name__ == "__main__":
    mcp.run()