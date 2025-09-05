import os
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP
from app import getEvents

# Initialize MCP server
mcp = FastMCP("call-for-papers-mcp")

@mcp.tool()
async def get_events(keywords: str, limit: int = 10) -> Dict[str, Any]:
    """Search for conferences matching specific keywords."""
    return getEvents(keywords, limit)

if __name__ == "__main__":
    # Check for transport type from environment variable
    transport = os.getenv("TRANSPORT", "stdio").lower()
    
    if transport == "http":
        # For HTTP deployment, use streamable-http transport
        mcp.run(transport="streamable-http")
    else:
        # Default to stdio transport for local development
        mcp.run(transport="stdio")
