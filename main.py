import os
from contextlib import asynccontextmanager
from fastmcp import FastMCP
from shared.db import pool
from database.init_db import init_db
from tools import classroom_tools, routine_tools, quiz_tools
from fastmcp.server.auth.providers.google import GoogleProvider

@asynccontextmanager
async def lifespan(server):
    await pool.open()
    await init_db()
    yield
    await pool.close()
'''   
auth = GoogleProvider(
    client_id=os.environ["GOOGLE_CLIENT_ID"],
    client_secret=os.environ["GOOGLE_CLIENT_SECRET"],
    base_url="https://helixion.fastmcp.app",
    required_scopes=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
    ],
)
''' 
mcp = FastMCP(name='academcp',lifespan=lifespan)

# all tools
routine_tools.register(mcp)
quiz_tools.register(mcp)
classroom_tools.register(mcp)


if __name__ == "__main__":
    #mcp.run()
    port = int(os.environ.get("PORT",8000))
    mcp.run(transport="streamable-http",host="0.0.0.0", port=port)
