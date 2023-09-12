import asyncio_demo
import aiohttp
import time
from spider import blog_spider


async def async_craw(url):
    print("craw url: ", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()
            print(f"craw url: {url}, {len(result)}")


loop = asyncio_demo.get_event_loop()

tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls]


start = time.time()
#  启动事件循环
loop.run_until_complete(asyncio_demo.wait(tasks))
end = time.time()
print("use time seconds: ", end - start)
