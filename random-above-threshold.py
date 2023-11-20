import asyncio
import random

c = (
    "\033[0m", # End of color
    "\033[36m", # Cyan
    "\033[91m", # Red
    "\033[35m", # Magenta
)

async def make_random(idx, threshold):
    print(c[idx+1] + f"Started randomizing {idx}")
    i=random.randint(0,10)
    while i<=threshold:
        print(c[idx+1] + f"Too low: {i}; retrying")
        await asyncio.sleep(1)
        i = random.randint(0,10)
    print(c[idx+1] + f"Finished randomizing with {i}")
    return i

async def main():
    res = await asyncio.gather(*(make_random(i, 10-i-1) for i in range(3)))
    return res

if __name__ == "__main__":
    random.seed(444)
    r1, r2,r3 = asyncio.run(main())
    print(f"{r1=}, {r2=}, {r3=}")
