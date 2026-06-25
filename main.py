from fastmcp import FastMCP
from shared.db import init_db
from tools import classroom_tools,routine_tools,quiz_tools


mcp = FastMCP(name='academcp')

init_db()

# all tools
routine_tools.register(mcp)
quiz_tools.register(mcp)
classroom_tools.register(mcp)


if __name__ == "__main__":
    mcp.run()
