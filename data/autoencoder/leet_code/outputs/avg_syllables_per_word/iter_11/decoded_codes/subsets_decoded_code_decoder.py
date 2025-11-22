from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        subsets_without_first = self.subsets(nums[1:])
        subsets_with_first = []
        for subset in subsets_without_first:
            subsets_with_first.append([nums[0]] + subset)
        return subsets_without_first + subsets_with_first