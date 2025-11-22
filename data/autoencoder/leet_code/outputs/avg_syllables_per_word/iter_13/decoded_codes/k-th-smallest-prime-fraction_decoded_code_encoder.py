import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []
        # Initialize heap with fractions having denominator as the last element
        for i in range(n - 1):
            fraction = arr[i] / arr[-1]
            heapq.heappush(min_heap, (fraction, i, n - 1))

        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            if j - 1 > i:
                new_fraction = arr[i] / arr[j - 1]
                heapq.heappush(min_heap, (new_fraction, i, j - 1))

        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]