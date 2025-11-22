import heapq
from collections import Counter

class Solution:
    def rearrangeString(self, s, k):
        if k <= 1:
            return s

        freq = Counter(s)

        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        wait_queue = []
        result = []

        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)

            wait_queue.append((count + 1, char))

            if len(wait_queue) == k:
                first_count, first_char = wait_queue.pop(0)
                if first_count < 0:
                    heapq.heappush(max_heap, (first_count, first_char))

        if len(result) != len(s):
            return ""

        return "".join(result)