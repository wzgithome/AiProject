from mcp import StdioServerParameters, stdio_server, ClientSession, stdio_client

import mcp.types as types

server_params=StdioServerParameters(
    command="python",
    args=["/Users/esired/Documents/python/AiProject/chapter06-agents/03-MCP_server.py"],
    env=None
)
async def handle_sapling_message(message:types.CreateMessageRequestParams)->types.CreateMessageResult:
    print(f'samping message:{message}')
    return types.CreateMessageResult(
        role="assistant",
        content=types.TextContent(
            type="text",
            text="hello,world!from model"
        ),
        model="qwen3.5-plus",
        stopReason="endTurn"
    )

async def run():
    async with stdio_client(server_params) as (read,write):
        async with ClientSession(read,write,sampling_callback=handle_sapling_message) as session:
            await session.initialize()
            prompts=await session.list_prompts()
            print(f'prompts：{prompts}')

            tools=await session.list_tools()
            print(f'tools:{tools}')

            resource=await session.list_resources()
            print(f'resources:{resource}')

            result=await session.call_tool("weather",{"city":"北京"})
            print(f'result:{result}')

if __name__ == '__main__':
    import asyncio
    asyncio.run(run())
