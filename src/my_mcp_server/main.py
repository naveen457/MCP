from fastmcp import FastMCP
import json
import random

mcp = FastMCP("My MCP Remote Server")


@mcp.tool()
def add_numbers(a: float, b: float) -> float:
    """Function used for addition."""
    return a + b


@mcp.tool()
def random_value(min_value: int, max_value: int) -> float:
    """Generate a random integer between the supplied bounds."""
    return random.randint(min_value, max_value)


@mcp.resource("info:/server")
def server_info():
    """Return server information."""
    data = {"name": "my mcp server", "version": "1.0.0", "data_created": "23/9/2026"}
    return json.dumps(data)


if __name__ == "__main__":
    mcp.run(transport="streamable-http", host="0.0.0.0", port=8000)
