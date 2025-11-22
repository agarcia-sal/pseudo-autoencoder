from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def maxSingleArray(nums: List[int], k: int) -> List[int]:
            drop = len(nums) - k
            stack = []
            for num in nums:
                while drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:k]

        def merge(arr1: List[int], arr2: List[int]) -> List[int]:
            result = []
            i, j = 0, 0
            while i < len(arr1) or j < len(arr2):
                # Compare slices lex order without slicing overhead
                if arr1[i:] > arr2[j:]:
                    result.append(arr1[i])
                    i += 1
                else:
                    result.append(arr2[j])
                    j += 1
            return result

        max_number = []
        for i in range(k + 1):
            if i <= len(nums1) and (k - i) <= len(nums2):
                candidate = merge(maxSingleArray(nums1, i), maxSingleArray(nums2, k - i))
                if candidate > max_number:
                    max_number = candidate
        return max_number