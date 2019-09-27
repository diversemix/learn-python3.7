#!/usr/bin/python3
from multiprocessing import Process, Queue
from queue import Empty
from typing import List


def process_batch(batch: List[str], result_list):
    c = [len(x) for x in batch]
    result_list.append(sum(c))


def read_batch(fd, n: int) -> List:
    data_array = []
    for counter in range(0, n):
        data = fd.readline()
        if data:
            data_array.append(data)
        else:
            break
    return data_array


def read_file(filename: str, q, n: int):
    with open(filename) as fd:
        ok = True
        while ok:
            data = read_batch(fd, n)
            q.put(data)
            ok = (len(data) == n)


def process_file(filename, fprocess):
    n = 2000
    results = []
    total_lines = 0
    q = Queue()
    p = Process(target=read_file, args=(filename, q, n, ))
    p.start()
    ok = True
    while ok:
        try:
            x = q.get(timeout=2)
            fprocess(x, results)
            lines = len(x)
            total_lines += lines
            ok = (lines == n)
        except Empty as e:
            print(e)
            ok = False
    p.join()
    return total_lines, sum(results)

if __name__ == '__main__':
    filename = 'test.txt'
    lines, chars = process_file(filename, process_batch)
    print(f"{lines} {chars} {filename}")
