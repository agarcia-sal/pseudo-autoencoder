import heapq
from typing import List

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []

        for i in range(n - 1):
            # heap elements: (fraction value, numerator index, denominator index)
            heapq.heappush(min_heap, (arr[i] / arr[n - 1], i, n - 1))

        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            if j - 1 > i:
                heapq.heappush(min_heap, (arr[i] / arr[j - 1], i, j - 1))

        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]