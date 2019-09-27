#!/usr/bin/python3
import time
import math
import asyncio
from dataclasses import dataclass
from typing import List

def process_batch(batch: List[str], clist):
    chars = 0
    for x in batch:
        # chars += len(x)
        chars += len(x)
    clist.append(chars)

async def async_process_batch(batch: List[str], clist):
    await asyncio.sleep(1)
    process_batch(batch, clist)

def read_batch(fd, n: int) -> List[str]:
    data_array = []
    for counter in range(0, n):
        data = fd.readline()
        if data:
            data_array.append(data)
        else:
          break
    return data_array


async def test(n):
    lines = 0
    chars = []
    task_process = None
    with open('test.txt') as fd:
        ok = True

        while ok:
            data = read_batch(fd, n)

            task_process = asyncio.create_task(async_process_batch(data, chars))
            # process_batch(data, chars) ; time.sleep(0.1)
            ok = (len(data) == n)
            lines += len(data)

    if task_process:
        await task_process
    return lines, sum(chars)

for n in [200, 2000, 8000]:
    start = time.time_ns()
    result = asyncio.run(test(n))
    elapsed1 = time.time_ns() - start
    print(result)
    print(f"Batches of {n} finished in {elapsed1/1e9} seconds")
