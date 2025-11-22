import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        # Use negative frequency for max-heap effect, words naturally sort lex order
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            freq_word = heapq.heappop(heap)
            result.append(freq_word[1])
        return result