from collections import Counter
from heapq import heapify, heappop

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)

        def build_heap(count):
            heap = []
            for word, freq in count.items():
                heap.append((-freq, word))
            heapify(heap)
            return heap

        heap = build_heap(count)

        result = []
        for _ in range(k):
            popped_element = heappop(heap)
            word = popped_element[1]
            result.append(word)

        return result