import asyncio

async def download(urls):
    for url in urls:
        print(f"Downloading page at {url} started")
        await asyncio.sleep(2) # simulating a page download
        print(f"Page downloaded from {url}")
        yield f"Page downloaded from url {url}"

async def main():
    results = []
    # "async for" does not automatically parallelize the iterations.
    # Instead it simply allows sequential iteration over an async
    # source. Use case for using "async for" is to iterate(without blocking
    # the event loop) over the
    # lines coming from a TCP stream, msgs from a websocket or
    # DB records from an async DB driver.
    async for i in download(["foo.com", "bar.com", "baz.com"]):
        results.append(i)

    print("All results:", results)

asyncio.run(main())