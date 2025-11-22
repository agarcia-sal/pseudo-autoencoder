from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    def reorganizeString(self, s):
        count = Counter(s)
        max_heap = []
        for char, freq in count.items():
            max_heap.append((-freq, char))
        heapify(max_heap)

        prev_char = None
        prev_freq = 0
        result = []

        while max_heap or prev_freq < 0:
            if not max_heap and prev_freq < 0:
                return ""
            freq, char = heappop(max_heap)
            result.append(char)
            freq += 1  # increment freq since freq is negative

            if prev_freq < 0:
                heappush(max_heap, (prev_freq, prev_char))

            prev_char = char
            prev_freq = freq

        return "".join(result)