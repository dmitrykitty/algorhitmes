import heapq
from pickletools import stringnl_noescape_pair, stringnl_noescape
from typing import List

data = [2, 7, 4, 1, 8]

def lastStoneweight(stones: List[int]) -> int:

    stones = [-x for x in stones]

    heapq.heapify(stones)

    while len(stones) > 1:
        print(stones)
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if first == second:
            continue
        heapq.heappush(stones, (first - second) if first < second else (second - first))

    return -stones[0] if stones else 0
print(lastStoneweight(data))