import heapq
from typing import List

class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        # Transform blocks into a min-heap for efficient extraction of smallest elements
        heapq.heapify(blocks)

        while len(blocks) > 1:
            first = heapq.heappop(blocks)
            second = heapq.heappop(blocks)
            combined_time = split + second
            heapq.heappush(blocks, combined_time)

        return blocks[0]