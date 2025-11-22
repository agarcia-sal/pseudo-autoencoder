from collections import Counter
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
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
                count_front, char_front = wait_queue.pop(0)
                if count_front < 0:
                    heapq.heappush(max_heap, (count_front, char_front))

        if len(result) != len(s):
            return ""

        return "".join(result)