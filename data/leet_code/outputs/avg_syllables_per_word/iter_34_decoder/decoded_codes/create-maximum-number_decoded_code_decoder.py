from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maxSingleArray(nums: List[int], k: int) -> List[int]:
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(arr1: List[int], arr2: List[int]) -> List[int]:
            result = []
            # Use lexicographical comparison for arrays; slice to compare
            while arr1 or arr2:
                # Compare remaining sequences lex order
                if arr1 > arr2:
                    result.append(arr1[0])
                    arr1 = arr1[1:]
                else:
                    result.append(arr2[0])
                    arr2 = arr2[1:]
            return result

        max_number = []
        len1, len2 = len(nums1), len(nums2)
        for i in range(k + 1):
            if i <= len1 and k - i <= len2:
                candidate = merge(maxSingleArray(nums1, i), maxSingleArray(nums2, k - i))
                if max_number < candidate:
                    max_number = candidate
        return max_number