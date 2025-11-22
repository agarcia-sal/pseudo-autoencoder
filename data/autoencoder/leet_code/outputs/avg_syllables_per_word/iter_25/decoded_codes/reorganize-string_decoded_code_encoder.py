import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = []

        for char, freq in count.items():
            heapq.heappush(max_heap, (-freq, char))

        prev_char = None
        prev_freq = 0
        result = []

        while max_heap or prev_freq < 0:
            if not max_heap and prev_freq < 0:
                return ""

            freq, char = heapq.heappop(max_heap)
            result.append(char)
            freq += 1  # Since freq is negative, incrementing moves toward zero

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            prev_char = char
            prev_freq = freq

        return "".join(result)