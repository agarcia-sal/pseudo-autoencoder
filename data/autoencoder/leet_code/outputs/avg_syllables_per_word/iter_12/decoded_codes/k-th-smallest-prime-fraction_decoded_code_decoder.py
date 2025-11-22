import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []

        # Initialize the heap with fractions (arr[i]/arr[n-1]) for i in [0, n-2]
        for i in range(n - 1):
            fraction_value = arr[i] / arr[-1]
            heapq.heappush(min_heap, (fraction_value, i, n - 1))

        # Extract the smallest fractions k-1 times
        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            if j - 1 > i:
                fraction_value = arr[i] / arr[j - 1]
                heapq.heappush(min_heap, (fraction_value, i, j - 1))

        # The k-th smallest fraction
        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]