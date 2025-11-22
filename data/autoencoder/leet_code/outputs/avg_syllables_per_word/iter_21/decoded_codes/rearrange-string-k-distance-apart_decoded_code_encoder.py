import heapq
from collections import Counter
from typing import List

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        freq = Counter(s)
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        wait_queue: List[tuple[int, str]] = []
        result: List[str] = []

        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            wait_queue.append((count + 1, char))  # decrement frequency

            if len(wait_queue) == k:
                cnt, ch = wait_queue.pop(0)
                if cnt < 0:
                    heapq.heappush(max_heap, (cnt, ch))

        if len(result) != len(s):
            return ""

        return "".join(result)