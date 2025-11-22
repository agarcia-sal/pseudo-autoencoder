import heapq
from collections import Counter, deque

class Solution:
    def rearrangeString(self, string_s: str, integer_k: int) -> str:
        if integer_k <= 1:
            return string_s

        frequency_counter = Counter(string_s)
        max_heap = [(-count, char) for char, count in frequency_counter.items()]
        heapq.heapify(max_heap)

        wait_queue = deque()
        result = []

        while max_heap:
            count_component, char_component = heapq.heappop(max_heap)
            result.append(char_component)
            wait_queue.append((count_component + 1, char_component))

            if len(wait_queue) == integer_k:
                count_head, char_head = wait_queue.popleft()
                if count_head < 0:
                    heapq.heappush(max_heap, (count_head, char_head))

        if len(result) != len(string_s):
            return ""

        return "".join(result)