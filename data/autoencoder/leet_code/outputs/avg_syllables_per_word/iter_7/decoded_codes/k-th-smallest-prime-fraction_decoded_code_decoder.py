from typing import List
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []

        # Initialize the heap with fractions having denominator as the last element
        for i in range(n - 1):
            heapq.heappush(min_heap, (arr[i] / arr[-1], i, n - 1))

        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            if j - 1 > i:
                heapq.heappush(min_heap, (arr[i] / arr[j - 1], i, j - 1))

        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]