import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2 or k <= 0:
            return []

        def minimum_of_two_values(value_one, value_two):
            if value_one < value_two:
                return value_one
            else:
                return value_two

        limit = minimum_of_two_values(k, len(nums1))
        min_heap = []

        for i in range(limit):
            first_sum = nums1[i] + nums2[0]
            heapq.heappush(min_heap, (first_sum, i, 0))

        result = []

        while min_heap and len(result) < k:
            _, i, j = heapq.heappop(min_heap)
            result.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                next_sum = nums1[i] + nums2[j + 1]
                heapq.heappush(min_heap, (next_sum, i, j + 1))

        return result