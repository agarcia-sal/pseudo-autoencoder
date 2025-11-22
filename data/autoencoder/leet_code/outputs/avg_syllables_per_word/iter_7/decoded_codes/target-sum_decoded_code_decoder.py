from typing import List, Dict, Tuple

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(index: int, current_sum: int, memo: Dict[Tuple[int, int], int]) -> int:
            if index == len(nums):
                return 1 if current_sum == target else 0
            if (index, current_sum) in memo:
                return memo[(index, current_sum)]
            positive = dfs(index + 1, current_sum + nums[index], memo)
            negative = dfs(index + 1, current_sum - nums[index], memo)
            memo[(index, current_sum)] = positive + negative
            return memo[(index, current_sum)]

        return dfs(0, 0, dict())