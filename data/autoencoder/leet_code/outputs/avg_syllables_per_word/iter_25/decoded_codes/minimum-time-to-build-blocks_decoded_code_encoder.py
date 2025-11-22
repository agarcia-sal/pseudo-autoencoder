import heapq
from typing import List

class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        # Transform list into a min-heap to always access the smallest elements efficiently
        heapq.heapify(blocks)
        while len(blocks) > 1:
            first = heapq.heappop(blocks)
            second = heapq.heappop(blocks)
            combined_time = split + second
            heapq.heappush(blocks, combined_time)
        return blocks[0] if blocks else 0