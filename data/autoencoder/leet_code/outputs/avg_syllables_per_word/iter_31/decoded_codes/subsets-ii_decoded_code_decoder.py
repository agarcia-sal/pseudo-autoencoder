from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        subset = []

        def dfs(i: int) -> None:
            if i >= len(nums):
                result.append(subset.copy())
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # Exclude nums[i] and skip duplicates
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return result