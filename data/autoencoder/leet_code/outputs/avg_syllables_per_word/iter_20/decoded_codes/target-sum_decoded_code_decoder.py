class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        def dfs(index: int, current_sum: int, memo: dict[tuple[int, int], int]) -> int:
            if index == len(nums):
                return 1 if current_sum == target else 0
            key = (index, current_sum)
            if key in memo:
                return memo[key]
            positive = dfs(index + 1, current_sum + nums[index], memo)
            negative = dfs(index + 1, current_sum - nums[index], memo)
            memo[key] = positive + negative
            return memo[key]

        return dfs(0, 0, {})