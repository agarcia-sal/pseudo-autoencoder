from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            # Place nums[i] to its correct position nums[nums[i]-1] if not already correct
            while nums[i] != nums[nums[i] - 1]:
                temp_first = nums[i]
                temp_second = nums[nums[i] - 1]
                nums[nums[i] - 1] = temp_first
                nums[i] = temp_second

        result_list = []
        for i, v in enumerate(nums):
            if v != i + 1:
                result_list.append(v)

        return result_list