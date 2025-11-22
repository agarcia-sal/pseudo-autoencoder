from heapq import heappush, heappop
from typing import List, Tuple

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        min_heap = []
        for i in range(n - 1):
            # Push initial fractions arr[i] / arr[n-1] with indices (i, n-1)
            self.helper_push_heap(min_heap, (arr[i] / arr[n - 1], i, n - 1))
        for _ in range(k - 1):
            val, i, j = self.helper_pop_heap(min_heap)
            if j - 1 > i:
                self.helper_push_heap(min_heap, (arr[i] / arr[j - 1], i, j - 1))
        val, i, j = self.helper_pop_heap(min_heap)
        return [arr[i], arr[j]]

    def helper_push_heap(self, min_heap: List[Tuple[float, int, int]], fraction: Tuple[float, int, int]) -> None:
        heappush(min_heap, fraction)

    def helper_pop_heap(self, min_heap: List[Tuple[float, int, int]]) -> Tuple[float, int, int]:
        return heappop(min_heap)