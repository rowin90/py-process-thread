import asyncio_demo
import aiohttp
from spider import blog_spider

semaphore = asyncio_demo.Semaphore(10)


async def async_craw(url):
    async with semaphore:
        print("craw url: ", url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                await asyncio_demo.sleep(5)
                print(f"craw url: {url}, {len(result)}")


loop = asyncio_demo.get_event_loop()

tasks = [
    loop.create_task(async_craw(url))
    for url in blog_spider.urls]

import time

start = time.time()
loop.run_until_complete(asyncio_demo.wait(tasks))
end = time.time()
print("use time seconds: ", end - start)
