import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []
        # Initialize the heap with fractions having the last element as denominator
        for i in range(n - 1):
            # Push tuple: (fraction value, numerator index, denominator index)
            heapq.heappush(min_heap, (arr[i] / arr[-1], i, n - 1))

        # Pop k-1 fractions, and push the next fraction in the row if possible
        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            if j - 1 > i:
                heapq.heappush(min_heap, (arr[i] / arr[j - 1], i, j - 1))

        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]