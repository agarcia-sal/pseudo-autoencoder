import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []

        # Initialize heap with fractions having the largest denominator (arr[n-1])
        for i in range(n - 1):
            heapq.heappush(min_heap, (arr[i] / arr[n - 1], i, n - 1))

        # Pop k-1 smallest fractions and push the next fraction with denominator decremented by 1 if valid
        for _ in range(k - 1):
            _, numerator_index, denominator_index = heapq.heappop(min_heap)
            if denominator_index - 1 > numerator_index:
                heapq.heappush(min_heap, (arr[numerator_index] / arr[denominator_index - 1], numerator_index, denominator_index - 1))

        _, numerator_index, denominator_index = heapq.heappop(min_heap)
        return [arr[numerator_index], arr[denominator_index]]