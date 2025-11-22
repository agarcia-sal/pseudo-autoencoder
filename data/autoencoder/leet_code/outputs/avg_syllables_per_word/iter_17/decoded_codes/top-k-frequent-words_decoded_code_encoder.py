from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = []
        for word, freq in count.items():
            heap.append((-freq, word))
        heapify(heap)
        result = []
        for _ in range(k):
            top_element = heappop(heap)
            result.append(top_element[1])
        return result