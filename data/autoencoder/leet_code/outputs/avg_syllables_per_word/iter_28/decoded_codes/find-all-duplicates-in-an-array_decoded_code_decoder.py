from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                j = nums[i] - 1
                nums[i], nums[j] = nums[j], nums[i]
        result_list = [v for i, v in enumerate(nums) if v != i + 1]
        return result_list