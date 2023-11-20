import asyncio


async def reverse_list(seq) -> list:
    await asyncio.sleep(max(seq))
    return list(reversed(seq))

async def main():
    task = asyncio.create_task(reverse_list([3,2,1]))
    print(task.done())  # prints False
    # await the completion of this task
    # otherwise it is possible that main()
    # completes execution before "task"
    # completes. Because asyncio.run(main()) calls
    # loop.run_until_complete(main()), the event loop
    # is only concerned (without `await task` present) that
    # main() is done, not that the tasks that get created
    # within main() are done. Without `await task`, the loop’s
    # other tasks will be cancelled, possibly before they are completed.
    # Instead of "await task" we could also use "await asyncio.gather(task)"
    # which ensures that task is completed before main() completes.
    res = await task
    #res = await asyncio.gather(task)
    print("Reversed list successful")
    print(task.done())  # prints True
    return res

res = asyncio.run(main())
print(res)