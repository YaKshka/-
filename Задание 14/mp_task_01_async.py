import threading
import time
import multiprocessing
import math
import requests
import asyncio
import aiohttp

# список url
urls = ['https://genshin-info.ru'] * 10


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def sequence():
    start_time = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        for url in urls:
            await fetch_url(session, url)
    end_time = time.perf_counter()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')


async def tasks():
    start_time = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            task = asyncio.create_task(fetch_url(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)
    end_time = time.perf_counter()
    print(f'threads time: {end_time - start_time: 0.2f} \n')

async def main():
    await sequence()
    await tasks()


if __name__ == '__main__':
    asyncio.run(main())
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        async time sequence:  0.49
        
        async timme tasks: 0.18
    """
