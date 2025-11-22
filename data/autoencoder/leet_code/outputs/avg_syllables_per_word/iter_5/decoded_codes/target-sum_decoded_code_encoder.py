class Solution:
    def findTargetSumWays(self, nums, target):
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def dfs(index, current_sum):
            if index == len(nums):
                return 1 if current_sum == target else 0
            return dfs(index + 1, current_sum + nums[index]) + dfs(index + 1, current_sum - nums[index])

        return dfs(0, 0)