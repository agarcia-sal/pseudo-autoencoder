import heapq
from typing import List

class Solution:
    def findKthLargest(self, list_of_numbers: List[int], K: int) -> int:
        min_heap = []
        for number in list_of_numbers:
            heapq.heappush(min_heap, number)
            if len(min_heap) > K:
                heapq.heappop(min_heap)
        return min_heap[0]