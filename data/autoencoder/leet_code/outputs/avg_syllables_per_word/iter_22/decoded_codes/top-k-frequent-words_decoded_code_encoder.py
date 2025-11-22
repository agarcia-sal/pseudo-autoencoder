from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for word, freq in count.items():
            # Push negative freq to get max heap behavior with min heap implementation
            heap.append((-freq, word))
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            _, word = heapq.heappop(heap)
            result.append(word)
        return result