from collections import Counter
from heapq import heapify, heappop, heappush

def least_interval(tasks, n):
    freq = Counter(tasks)
    max_heap = [-c for c in freq.values()]
    heapify(max_heap)
    time = 0
    queue = []  # holds (ready_time, count)

    while max_heap or queue:
        while queue and queue[0][0] == time:
            _, c = queue.pop(0)
            if c < 0:
                heappush(max_heap, c)
        if max_heap:
            c = heappop(max_heap) + 1
            if c < 0:
                queue.append((time + n + 1, c))
        time += 1

    return time