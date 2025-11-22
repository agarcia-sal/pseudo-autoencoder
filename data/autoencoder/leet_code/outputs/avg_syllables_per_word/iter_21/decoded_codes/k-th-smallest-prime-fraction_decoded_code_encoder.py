import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []
        # Initialize heap with fractions arr[i]/arr[n-1] for i in [0, n-2]
        for i in range(n - 1):
            heapq.heappush(min_heap, (arr[i] / arr[-1], i, n - 1))
        # Pop k-1 fractions from heap and push next fractions in sequence
        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            if j - 1 > i:
                heapq.heappush(min_heap, (arr[i] / arr[j - 1], i, j - 1))
        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]