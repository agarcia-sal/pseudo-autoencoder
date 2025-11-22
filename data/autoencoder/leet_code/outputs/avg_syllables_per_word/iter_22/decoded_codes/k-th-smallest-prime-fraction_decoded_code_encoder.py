import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
        n = len(arr)
        min_heap = []
        # Initialize heap with fractions formed with the last element as denominator
        for i in range(n - 1):
            heapq.heappush(min_heap, (arr[i] / arr[-1], i, n - 1))
        # Extract k-1 smallest fractions and push next possible fractions
        for _ in range(k - 1):
            _, i, j = heapq.heappop(min_heap)
            if j - 1 > i:
                heapq.heappush(min_heap, (arr[i] / arr[j - 1], i, j - 1))
        # The k-th smallest fraction
        _, i, j = heapq.heappop(min_heap)
        return [arr[i], arr[j]]