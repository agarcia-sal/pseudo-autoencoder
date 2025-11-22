import heapq
from collections import Counter, deque

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        freq = Counter(s)
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        wait_queue = deque()  # hold pairs of (count, char) waiting for k interval
        result = []

        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)
            # increment count since we use negative counts for max heap
            wait_queue.append((count + 1, char))

            if len(wait_queue) == k:
                old_count, old_char = wait_queue.popleft()
                if old_count < 0:
                    heapq.heappush(max_heap, (old_count, old_char))

        if len(result) != len(s):
            return ""
        return "".join(result)