import heapq
from typing import List

class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heap = blocks[:]
        heapq.heapify(heap)
        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            combined_time = split + second
            heapq.heappush(heap, combined_time)
        return heap[0]