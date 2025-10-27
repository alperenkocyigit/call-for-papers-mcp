import os
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP
from starlette.middleware.cors import CORSMiddleware
import uvicorn
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
        # For Smithery deployment, use streamable HTTP transport
        app = mcp.streamable_http_app()
        
        # Add CORS middleware for cross-origin requests
        from starlette.applications import Starlette
        from starlette.middleware import Middleware
        
        # Wrap the app with CORS middleware
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "OPTIONS"],
            allow_headers=["*"],
            expose_headers=["mcp-session-id", "mcp-protocol-version"],
            max_age=86400,
        )
        
        # Get port from environment variable
        port = int(os.getenv("PORT", 8000))
        
        print(f"Starting server on http://0.0.0.0:{port}")
        print("Available endpoints:")
        for route in app.routes:
            print(f"  {route.path}")
        
        # Run the server
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=port,
            log_level="info"
        )
    else:
        # Default to stdio transport for local development
        mcp.run(transport="stdio")
