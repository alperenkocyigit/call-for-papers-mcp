from typing import Dict, Any
from mcp.server.fastmcp import FastMCP
from app import getEvents

# Initialize MCP server for HTTP transport
mcp = FastMCP("call-for-papers-mcp", host="0.0.0.0", port=8000)

@mcp.tool()
async def get_events(keywords: str, limit: int = 10) -> Dict[str, Any]:
    """Search for conferences matching specific keywords."""
    return getEvents(keywords, limit)

if __name__ == "__main__":
    # Use HTTP transport instead of stdio
    mcp.run(transport="streamable-http")
