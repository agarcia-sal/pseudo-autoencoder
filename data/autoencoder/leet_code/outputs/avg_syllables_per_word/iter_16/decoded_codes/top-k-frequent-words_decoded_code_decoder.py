import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result