# 自己封装一个MCP服务端
from mcp.server.fastmcp import FastMCP

mcp=FastMCP('mymcpdemo')

@mcp.tool()
def add(a:int,b:int)->int:
    """两个数求和"""
    print(f'my mcp demo called:add{a},{b}')
    return a+b

@mcp.tool()
def weather(city:str)->str:
    """获取某个城市的天气"""
    return '城市：'+city+'，今天天气不错'

# 可以把 @mcp.resource
# 看作 Flask 中的 @app.route('/greeting/<name>')，
# 只是它遵循 MCP 协议而非 HTTP 协议。
@mcp.resource("greeting://{name}")
def greeting(name:str)->str:
    """Greet a person by name"""
    print(f'my mcp demo called:greeting({name})')
    return f'Hello,{name}'

if __name__ == '__main__':
    # 以sse协议暴露服务(推荐)
    # mcp.run(transport='sse')
    # 以stdio协议暴露服务
    mcp.run(transport='stdio')