import heapq
from typing import List

class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        # Initialize a min-heap from the blocks list
        heap = blocks[:]
        heapq.heapify(heap)

        # Combine the two smallest elements until only one remains
        while len(heap) > 1:
            first_element = heapq.heappop(heap)
            second_element = heapq.heappop(heap)
            combined_time = split + second_element
            heapq.heappush(heap, combined_time)

        return heap[0] if heap else 0