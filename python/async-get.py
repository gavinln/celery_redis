import asyncio
from aiohttp import ClientSession

async def hello(url):
    with ClientSession() as session:
        async with session.get(url) as response:
            response = await response.text()
            print(len(response))

loop = asyncio.get_event_loop()
loop.run_until_complete(hello("http://httpbin.org/get"))
