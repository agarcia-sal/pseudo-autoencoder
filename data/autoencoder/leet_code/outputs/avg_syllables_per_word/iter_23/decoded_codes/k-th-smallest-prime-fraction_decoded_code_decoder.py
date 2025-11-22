import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []

        # Initialize the heap with fractions where denominator is the last element
        for i in range(n - 1):
            # Store tuples as (fraction value, numerator index i, denominator index j)
            heapq.heappush(min_heap, (arr[i] / arr[n - 1], i, n - 1))

        # Extract k-1 fractions to reach the kth smallest
        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            if j - 1 > i:
                # Push the next fraction with denominator index decremented by 1
                heapq.heappush(min_heap, (arr[i] / arr[j - 1], i, j - 1))

        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]