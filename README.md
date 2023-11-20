## Notes on asyncio constructs:

- Event loop: You can think of an event loop as something like a `while True` loop that monitors coroutines, taking feedback on what’s idle, and looking around for things that can be executed in the meantime. It is able to wake up an idle coroutine when whatever that coroutine is waiting on becomes available.
- `asyncio.run()`, introduced in Python 3.7, is responsible for getting the event loop, running tasks until they are marked as complete, and then closing the event loop.
- Coroutines don’t do much on their own until they are tied to the event loop.
- By default, an async IO event loop runs in a single thread and on a single CPU core. Usually, running one single-threaded event loop in one CPU core is more than sufficient. It is also possible to run event loops across multiple cores.
- `async for` does not automatically parallelize the iterations. Instead it simply allows sequential iteration over an async source. Use case for using "async for" is to iterate(without blocking the event loop) over the lines coming from a TCP stream, msgs from a websocket or DB records from an async DB driver.