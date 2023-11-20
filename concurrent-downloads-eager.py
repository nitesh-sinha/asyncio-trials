import asyncio
import random

async def download(url):
    print(f"Downloading page at {url} started")
    i = random.randint(0,3)
    await asyncio.sleep(i) # simulating a page download
    print(f"Page downloaded from {url}")
    return f"Page downloaded from url {url}"

async def main():
    # asyncio.as_completed runs all the coroutines download() concurrently
    # and processes the results as they arrive
    for f in asyncio.as_completed([download(x) for x in ["foo.com", "bar.com", "baz.com"]]):
        result = await f
        print(f"Result arrived: {result}")

asyncio.run(main())
