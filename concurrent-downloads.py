import asyncio

async def download(url):
    print(f"Downloading page at {url} started")
    await asyncio.sleep(1) # simulating a page download
    print(f"Page downloaded from {url}")
    return f"Page downloaded from url {url}"

async def main():
    # asyncio.gather runs the coroutines download() concurrently
    # and processes the results when all are done
    results = await asyncio.gather(*[download(x) for x in ["foo.com", "bar.com", "baz.com"]])
    print(results)

asyncio.run(main())
