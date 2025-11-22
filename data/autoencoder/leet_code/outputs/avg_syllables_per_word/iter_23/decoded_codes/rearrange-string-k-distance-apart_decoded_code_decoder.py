from collections import Counter, deque
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if k <= 1:
            return s

        freq = Counter(s)
        # max_heap of pairs (-count, char)
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)

        wait_queue = deque()  # store pairs (count, char) waiting to be re-added to heap
        result = []

        while max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)

            # decrement count (note count is negative)
            wait_queue.append((count + 1, char))

            if len(wait_queue) == k:
                count_front, char_front = wait_queue.popleft()
                if count_front < 0:
                    heapq.heappush(max_heap, (count_front, char_front))

        if len(result) != len(s):
            return ""

        return "".join(result)