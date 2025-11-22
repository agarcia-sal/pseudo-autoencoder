import heapq
from typing import List

class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        # Convert the list into a min-heap in-place
        heapq.heapify(blocks)

        # Combine blocks until only one remains
        while len(blocks) > 1:
            first = heapq.heappop(blocks)
            second = heapq.heappop(blocks)
            combined_time = split + second
            heapq.heappush(blocks, combined_time)

        # Return the remaining element
        return blocks[0] if blocks else 0