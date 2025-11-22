from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        subsets_without_first = self.subsets(nums[1:])
        subsets_with_first = []
        first = nums[0]
        for subset in subsets_without_first:
            subsets_with_first.append([first] + subset)
        return subsets_without_first + subsets_with_first