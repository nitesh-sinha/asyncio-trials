import asyncio
import time
import random

# Each call to count() coroutine will have its
# unique local variable r
async def count():
    r = random.randint(0,9)
    print(f"Random start {r}")
    await asyncio.sleep(1)
    print(f"Random end {r}")


# await cannot be used outside of an
# `async def` coroutine
async def main():
    await asyncio.gather(*[count() for i in range(3)])
    #await count() # await can only be called on an awaitable object - i.e. another coroutine or an obj defining .__await__() method

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start
    print(f"Executed in {elapsed} seconds")
