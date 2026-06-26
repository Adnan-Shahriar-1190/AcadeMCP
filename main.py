import os
from contextlib import asynccontextmanager
from fastmcp import FastMCP
from shared.db import pool
from database.init_db import init_db
from tools import classroom_tools, routine_tools, quiz_tools


@asynccontextmanager
async def lifespan(server):
    print("🚀 Starting AcademCP...")
    print(f"Database URL exists: {bool(os.getenv('DB_URL'))}")
    
    try:
        await pool.open()
        print("✅ Pool opened successfully")
        
        await init_db()
        print("✅ init_db completed")
        
        yield
    except Exception as e:
        print(f"❌ STARTUP FAILED: {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
        raise
    finally:
        await pool.close()


mcp = FastMCP(name='academcp', lifespan=lifespan)

routine_tools.register(mcp)
quiz_tools.register(mcp)
classroom_tools.register(mcp)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run(transport="streamable-http", host="0.0.0.0", port=port)