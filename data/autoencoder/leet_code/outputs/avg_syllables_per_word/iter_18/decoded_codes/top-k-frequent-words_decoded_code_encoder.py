from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        count = Counter(words)
        heap = []

        for word, freq in count.items():
            heap.append((-freq, word))
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            freq_neg, word = heapq.heappop(heap)
            result.append(word)

        return result