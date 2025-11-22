import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        # Heap elements: (-frequency, word) to get max frequency with min-heap,
        # and lex order among words with same frequency (since Python compares tuple elements lex order)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            freq, word = heapq.heappop(heap)
            result.append(word)
        return result