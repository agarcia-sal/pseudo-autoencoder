from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []

        def dfs(i: int):
            if i >= len(nums):
                result.append(subset.copy())
                return
            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return result