from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        max_heap = [(-freq, ch) for ch, freq in count.items()]
        heapq.heapify(max_heap)

        previous_character = None
        previous_frequency = 0
        result = []

        while max_heap or previous_frequency < 0:
            if not max_heap and previous_frequency < 0:
                return ""

            current_frequency, current_character = heapq.heappop(max_heap)
            result.append(current_character)
            current_frequency += 1  # since frequencies are negative, incrementing means "using one occurrence"

            if previous_frequency < 0:
                heapq.heappush(max_heap, (previous_frequency, previous_character))

            previous_character = current_character
            previous_frequency = current_frequency

        return "".join(result)