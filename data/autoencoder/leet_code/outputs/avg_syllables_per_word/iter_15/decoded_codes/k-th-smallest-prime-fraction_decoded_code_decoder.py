import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []
        # Initialize heap with fractions having denominator as the largest element
        for i in range(n - 1):
            # Heap stores tuples of (fraction_value, numerator_index, denominator_index)
            heapq.heappush(min_heap, (arr[i] / arr[-1], i, n - 1))
        # Pop k-1 smallest fractions from the heap
        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            if j - 1 > i:
                heapq.heappush(min_heap, (arr[i] / arr[j - 1], i, j - 1))
        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]