import heapq
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            _, word = heapq.heappop(heap)
            result.append(word)
        return result