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
            merged_list = []
            while arr1 or arr2:
                # Comparing lex order starting from current positions
                if arr1 > arr2:
                    merged_list.append(arr1[0])
                    arr1 = arr1[1:]
                else:
                    merged_list.append(arr2[0])
                    arr2 = arr2[1:]
            return merged_list

        max_number = []
        len1, len2 = len(nums1), len(nums2)
        for i in range(k + 1):
            if i <= len1 and (k - i) <= len2:
                candidate = merge(maxSingleArray(nums1, i), maxSingleArray(nums2, k - i))
                if candidate > max_number:
                    max_number = candidate
        return max_number