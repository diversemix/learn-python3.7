import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main1():
    start = time.time_ns()
    await say_after(1, 'hello')
    await say_after(2, 'world')

    elapsed = time.time_ns() - start
    print(f"1) finished in {elapsed/1e9} seconds")


async def main2():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    start = time.time_ns()
    await task1
    await task2

    elapsed = time.time_ns() - start
    print(f"2) finished in {elapsed/1e9} seconds")


asyncio.run(main1())
asyncio.run(main2())