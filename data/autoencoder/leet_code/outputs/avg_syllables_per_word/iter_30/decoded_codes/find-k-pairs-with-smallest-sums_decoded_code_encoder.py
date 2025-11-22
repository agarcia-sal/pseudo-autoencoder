import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []

        min_heap = []
        # Initialize heap with pairs (nums1[i] + nums2[0], i, 0)
        for i in range(min(k, len(nums1))):
            heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

        result = []
        while min_heap and len(result) < k:
            sum_value, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                # Push next pair (nums1[i] + nums2[j+1], i, j+1)
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i, j + 1))

        return result