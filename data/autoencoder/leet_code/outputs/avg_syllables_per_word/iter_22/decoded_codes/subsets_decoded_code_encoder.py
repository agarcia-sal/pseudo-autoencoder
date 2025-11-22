class Solution:
    def subsets(self, nums):
        if len(nums) == 0:
            return [[]]
        subsets_without_first = self.subsets(nums[1:])
        subsets_with_first = []
        for subset in subsets_without_first:
            new_subset = [nums[0]] + subset
            subsets_with_first.append(new_subset)
        return subsets_without_first + subsets_with_first