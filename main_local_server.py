import random
from fastmcp import FastMCP

# Step 1 - Create an instance of the server with its name
mcp = FastMCP("demo-server")

# Step 2 - Create the tools using decorator of the instance created 
@mcp.tool
def roll_dice(n_dice: int=1) -> list[int]:
    """Roll n_dice 6-sided dice and return the results."""
    return  [random.randint(1, 6) for _ in range(n_dice)]

@mcp.tool
def add_numbers(a: float, b: float) -> float:
    """Add two number and return its value"""
    return a + b

# Step 3 - Running the server
if __name__ == "__main__" :
    mcp.run()

# Step 4 - Testing the server using the mcp inspector
# uv run fastmcp dev <file name.py>

# Step 5 - Running the server
# uv run fastmcp run <file name.py>

# Step 6 (Optional) - Deploy on a Host (Claude Desktop)
# uv run fastmcp install claude-desktop <file name.py>

"""

if error comes , then in the config file , change the path of uv by the absolute path 
use command  - where uv in cmd and copy paste in config and restart claude

"""