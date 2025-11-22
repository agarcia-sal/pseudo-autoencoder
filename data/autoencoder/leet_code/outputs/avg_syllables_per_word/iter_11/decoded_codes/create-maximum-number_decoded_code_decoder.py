from collections import deque

class Solution:
    def maxNumber(self, nums1, nums2, k):
        def maxSingleArray(nums, k):
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(arr1, arr2):
            arr1 = deque(arr1)
            arr2 = deque(arr2)
            merged_list = []
            while arr1 or arr2:
                if arr1 > arr2:
                    merged_list.append(arr1.popleft())
                else:
                    merged_list.append(arr2.popleft())
            return merged_list

        max_number = []
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                candidate = merge(maxSingleArray(nums1, i), maxSingleArray(nums2, k - i))
                if max_number < candidate:
                    max_number = candidate
        return max_number