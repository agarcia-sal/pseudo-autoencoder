import heapq
from collections import Counter, deque

def rearrange_string_k_distance(s, k):
    if k <= 1:
        return s

    freq = Counter(s)
    max_heap = [(-count, ch) for ch, count in freq.items()]
    heapq.heapify(max_heap)

    wait = deque()
    res = []

    while max_heap:
        c, ch = heapq.heappop(max_heap)
        res.append(ch)
        wait.append((c + 1, ch))
        if len(wait) == k:
            c2, ch2 = wait.popleft()
            if c2 < 0:
                heapq.heappush(max_heap, (c2, ch2))

    return "" if len(res) != len(s) else "".join(res)