import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, words, k):
        count = Counter(words)
        heap = []
        for word, freq in count.items():
            # Push (-freq, word) so the heap sorts by highest frequency and then lex order
            heap.append((-freq, word))
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            _, word = heapq.heappop(heap)
            result.append(word)
        return result