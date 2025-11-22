from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        n = len(nums)
        dp = self.initialize_dp(target)

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]

    def initialize_dp(self, target: int) -> List[bool]:
        dp = [False] * (target + 1)
        dp[0] = True
        return dp