from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        # max_heap stores pairs of (-frequency, character)
        max_heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(max_heap)

        prev_char = None
        prev_freq = 0
        result = []

        while max_heap or prev_freq < 0:
            if not max_heap and prev_freq < 0:
                return ""
            freq, ch = heapq.heappop(max_heap)
            result.append(ch)
            freq += 1  # since freq is negative, increment means adding one (towards zero)

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            prev_char = ch
            prev_freq = freq

        return "".join(result)