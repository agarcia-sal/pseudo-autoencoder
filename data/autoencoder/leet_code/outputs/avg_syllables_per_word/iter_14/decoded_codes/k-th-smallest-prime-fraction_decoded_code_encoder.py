import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []

        # Initialize the min heap with fractions arr[i]/arr[n-1]
        for i in range(n - 1):
            fraction = arr[i] / arr[-1]
            # Heap elements are tuples: (fraction value, numerator index i, denominator index j)
            heapq.heappush(min_heap, (fraction, i, n - 1))

        # Extract the smallest fraction k-1 times
        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            # If possible, push the next fraction with denominator index decremented by 1
            if j - 1 > i:
                fraction = arr[i] / arr[j - 1]
                heapq.heappush(min_heap, (fraction, i, j - 1))

        # The kth smallest fraction is now at the top of the heap
        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]