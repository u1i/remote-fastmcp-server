import asyncio
import logging
from fastmcp import FastMCP

logger = logging.getLogger(__name__)
logging.basicConfig(format="[%(levelname)s]: %(message)s", level=logging.INFO)

# Initialize your FastMCP server
mcp = FastMCP("MyRemoteMathServer")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Use this to add two numbers together. You MUST use this tool when asked to perform additions"""
    logger.info(f"Received add request: a={a}, b={b}")
    return a + b

if __name__ == "__main__":
    # To run remotely using Streamable HTTP
    # You would typically bind to '0.0.0.0' to be accessible from other machines
    # and use an available port (e.g., 8000)
    print("Starting FastMCP server for remote access...")
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
    print("FastMCP server stopped.")
