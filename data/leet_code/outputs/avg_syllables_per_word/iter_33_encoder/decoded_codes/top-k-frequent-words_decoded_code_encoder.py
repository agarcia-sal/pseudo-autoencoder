from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        heap = []
        for word, freq in count.items():
            # Push (-freq, word) so that heapq pops the highest frequency first,
            # and for ties, lex order smallest word.
            heap.append((-freq, word))
        heapq.heapify(heap)
        result = []
        for _ in range(k):
            freq_word = heapq.heappop(heap)
            result.append(freq_word[1])
        return result