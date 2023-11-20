import asyncio
import random
import time

async def cook_burgers(customer: str):
    num_burgers = random.randint(1,5)
    print(f"Cooking {num_burgers} burgers for {customer}")
    await asyncio.sleep(num_burgers)
    print(f"Done cooking {num_burgers} burgers for {customer}")
    return num_burgers

async def cook_fries(num_burgers: int, customer: str):
    num_fries = random.randint(num_burgers, 10)
    print(f"Cooking {num_fries} fries for {customer}")
    await asyncio.sleep(num_fries)
    print(f"Done cooking {num_fries} fries for {customer}")
    return num_fries

async def prepare_meal(customer: str):
    start = time.perf_counter()
    res1 = await cook_burgers(customer)
    res2 = await cook_fries(res1, customer)
    duration = time.perf_counter() - start
    print(f"Finished cooking {res1} burgers and {res2} fries in {duration} seconds for {customer}!")


async def main():
    customers = ["BB", "TY", "FEI"]
    await asyncio.gather(*[prepare_meal(customer) for customer in customers])

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    duration= time.perf_counter() - start
    print(f"Done cooking all the food in {duration} seconds!!")