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
            i, j = 0, 0
            # Use deque for efficient pop from front or just indices
            while i < len(arr1) or j < len(arr2):
                # Compare slices lex order without costly slicing: use indices
                if arr1[i:] > arr2[j:]:
                    merged_list.append(arr1[i])
                    i += 1
                else:
                    merged_list.append(arr2[j])
                    j += 1
            return merged_list

        max_number = []
        len1, len2 = len(nums1), len(nums2)
        for i in range(k + 1):
            if i <= len1 and (k - i) <= len2:
                candidate = merge(maxSingleArray(nums1, i), maxSingleArray(nums2, k - i))
                if candidate > max_number:
                    max_number = candidate
        return max_number