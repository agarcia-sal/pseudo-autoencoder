from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # Sort a copy of nums to avoid in-place modification issues during assignment
        sorted_nums = sorted(nums)
        n = len(nums)
        left = (n - 1) // 2
        right = n - 1

        for i in range(n):
            if i % 2 == 0:
                nums[i] = sorted_nums[left]
                left -= 1
            else:
                nums[i] = sorted_nums[right]
                right -= 1