import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result