from collections import deque

class Solution:
    def maxNumber(self, nums1, nums2, k):
        def maxSingleArray(nums, k):
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(arr1, arr2):
            merged_list = []
            arr1, arr2 = deque(arr1), deque(arr2)
            while arr1 or arr2:
                if arr1 > arr2:
                    merged_list.append(arr1.popleft())
                else:
                    merged_list.append(arr2.popleft())
            return merged_list

        max_number = []
        len1, len2 = len(nums1), len(nums2)
        for i in range(k + 1):
            if i <= len1 and k - i <= len2:
                candidate = merge(maxSingleArray(nums1, i), maxSingleArray(nums2, k - i))
                if max_number < candidate:
                    max_number = candidate
        return max_number