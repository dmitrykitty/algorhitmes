import sys, os, heapq
from typing import List


def leastInterval(tasks: List[str], n: int) -> int:
    counts = {}  # zliczanie elementow
    for task in tasks:
        if task in counts:
            counts[task] += 1
        else:
            counts[task] = 1

    max_heap = [(-count, task) for task, count in counts.items()]
    heapq.heapify(max_heap)
    # heapify elemetow wg pierszego, później wg drugiegi i tk dalej
    waiting_tasks = []
    interval_count = 0
    while max_heap or waiting_tasks:  # bo pusta krotka da False
        waiting_tasks = []
        cycles, i = 0, 0

        for _ in range(n + 1):  # samo zadanie jako 1 + przerwa długością n
            if max_heap:  # jak jeszcze są krotki - pobieramy z maks. iloscia wystapien
                count, task = heapq.heappop(max_heap)
                if count < -1:  # jak zostao więcej niż jedno zadanie
                    waiting_tasks.append((count + 1, task))
                cycles += 1  # zwiekszamy jak nie wystąpił break
            elif not waiting_tasks:
                break  # jak nie ma taskow do zrobienia i nie ma waiting tasks
            else:
                cycles += 1

        for task in waiting_tasks:
            heapq.heappush(max_heap, task)  # zwracamy krotkę już ze zmniejszoną ilością wystąpien taska

        interval_count += (n + 1) if max_heap else cycles  # jak jeszcze pozostały taski - był pełny cycl n+1

    return interval_count


tasks = "D H E B D G G J B F F J G J A G G B F J H C D F C I A B H A D J H G H J".split()
print(leastInterval(tasks, 2))
