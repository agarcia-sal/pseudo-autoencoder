import heapq
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)  # word -> frequency
        heap = []
        for word, freq in count.items():
            # Push (-freq, word) to build a max-heap by frequency
            # and lex order naturally because heapq in Python uses tuple ordering
            heap.append((-freq, word))
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            top_element = heapq.heappop(heap)
            result.append(top_element[1])

        return result