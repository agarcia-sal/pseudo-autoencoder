import heapq
from typing import List, Tuple

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []

        min_heap: List[Tuple[int, int, int]] = []

        # Initialize the heap with the first element in nums2 paired with the first k elements in nums1
        for i in range(min(k, len(nums1))):
            sum_of_elements = nums1[i] + nums2[0]
            heapq.heappush(min_heap, (sum_of_elements, i, 0))

        result: List[List[int]] = []

        while min_heap and len(result) < k:
            _, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])

            if j + 1 < len(nums2):
                next_sum = nums1[i] + nums2[j + 1]
                heapq.heappush(min_heap, (next_sum, i, j + 1))

        return result