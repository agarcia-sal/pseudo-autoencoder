from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            _, current_word = heapq.heappop(heap)
            result.append(current_word)
        return result