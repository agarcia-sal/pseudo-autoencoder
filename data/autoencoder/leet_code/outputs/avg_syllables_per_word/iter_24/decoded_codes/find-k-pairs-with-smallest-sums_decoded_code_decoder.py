import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []

        min_heap = []
        for i in range(min(k, len(nums1))):
            sum_of_pair = nums1[i] + nums2[0]
            heapq.heappush(min_heap, (sum_of_pair, i, 0))

        result = []
        while min_heap and len(result) < k:
            sum_value, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            next_index = j + 1
            if next_index < len(nums2):
                next_sum = nums1[i] + nums2[next_index]
                heapq.heappush(min_heap, (next_sum, i, next_index))

        return result