from fastmcp import FastMCP
import math

mcp = FastMCP(name='academcp')

@mcp.tool
def add_apples(num1:int,num2:int)->int:
    return (math.pow(num1,2) + num2)

if __name__ == "__main__":
    mcp.run()
