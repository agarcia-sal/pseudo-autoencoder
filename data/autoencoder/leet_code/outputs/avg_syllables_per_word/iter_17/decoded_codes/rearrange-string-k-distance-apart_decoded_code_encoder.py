from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        freq = Counter(s)
        max_heap = [(-count, char) for char, count in freq.items()]
        heapify(max_heap)

        wait_queue = []
        result = []

        while max_heap:
            count, char = heappop(max_heap)
            result.append(char)
            wait_queue.append((count + 1, char))

            if len(wait_queue) == k:
                front_count, front_char = wait_queue.pop(0)
                if front_count < 0:
                    heappush(max_heap, (front_count, front_char))

        if len(result) != len(s):
            return ""

        return "".join(result)