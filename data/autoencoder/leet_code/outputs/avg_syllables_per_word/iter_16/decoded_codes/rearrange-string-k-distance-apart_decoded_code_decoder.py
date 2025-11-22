import heapq
from collections import Counter, deque

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        freq = Counter(s)
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        wait_queue = deque()
        result = []

        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            wait_queue.append((count + 1, char))  # increment count since one instance used

            if len(wait_queue) == k:
                cnt, ch = wait_queue.popleft()
                if cnt < 0:
                    heapq.heappush(max_heap, (cnt, ch))

        if len(result) != len(s):
            return ""

        return "".join(result)