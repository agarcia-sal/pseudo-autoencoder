from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)

        prev_char, prev_freq = None, 0
        result = []

        while max_heap or prev_freq < 0:
            if not max_heap and prev_freq < 0:
                return ""
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            freq += 1

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            prev_char, prev_freq = char, freq

        return "".join(result)