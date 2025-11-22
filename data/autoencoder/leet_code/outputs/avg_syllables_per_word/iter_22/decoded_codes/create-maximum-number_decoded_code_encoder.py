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
            # Compare lex order of the remaining arrays to decide which element to pick
            while arr1 or arr2:
                # Python lexicographic comparison of lists works natively
                if arr1 > arr2:
                    result.append(arr1.pop(0))
                else:
                    result.append(arr2.pop(0))
            return result

        max_number = []
        for i in range(k + 1):
            if i <= len(nums1) and k - i <= len(nums2):
                candidate = merge(maxSingleArray(nums1, i), maxSingleArray(nums2, k - i))
                if candidate > max_number:
                    max_number = candidate
        return max_number