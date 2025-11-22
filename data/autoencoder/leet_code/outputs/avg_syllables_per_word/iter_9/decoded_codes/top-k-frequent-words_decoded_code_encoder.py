from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapify(heap)
        result = [heappop(heap)[1] for _ in range(k)]
        return result