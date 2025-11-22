import heapq
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        count = self.count_frequency(s)
        max_heap = self.build_max_heap(count)

        prev_char = None
        prev_freq = 0
        result = []

        while max_heap or prev_freq < 0:
            if not max_heap and prev_freq < 0:
                return ""
            freq, char = self.pop_from_heap(max_heap)
            result.append(char)
            freq += 1
            if prev_freq < 0:
                self.push_to_heap(max_heap, prev_freq, prev_char)
            prev_char = char
            prev_freq = freq

        return self.join_characters(result)

    def count_frequency(self, s: str) -> dict:
        return dict(Counter(s))

    def build_max_heap(self, count: dict) -> list:
        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)
        return max_heap

    def pop_from_heap(self, max_heap: list) -> tuple:
        return heapq.heappop(max_heap)

    def push_to_heap(self, max_heap: list, freq: int, char: str) -> None:
        heapq.heappush(max_heap, (freq, char))

    def join_characters(self, list_of_characters: list) -> str:
        return "".join(list_of_characters)