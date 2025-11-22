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
            result = []
            # Use deque for efficient pops from the front
            dq1, dq2 = deque(arr1), deque(arr2)
            while dq1 or dq2:
                # Compare remaining sequences lex order to determine which to pop from
                if list(dq1) > list(dq2):
                    result.append(dq1.popleft())
                else:
                    result.append(dq2.popleft())
            return result

        max_number = []
        len1, len2 = len(nums1), len(nums2)
        for i in range(k + 1):
            if i <= len1 and k - i <= len2:
                candidate = merge(maxSingleArray(nums1, i), maxSingleArray(nums2, k - i))
                if candidate > max_number:
                    max_number = candidate
        return max_number