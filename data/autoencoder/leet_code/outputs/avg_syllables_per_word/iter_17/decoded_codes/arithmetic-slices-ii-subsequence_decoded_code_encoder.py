from collections import defaultdict
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        dp = self.initialize_dp(n)
        total_count = 0

        for i in range(n):
            for j in range(i):
                d = self.calculate_difference(nums[i], nums[j])
                if d in dp[j]:
                    dp[i][d] += dp[j][d] + 1
                    total_count += dp[j][d]
                else:
                    dp[i][d] += 1

        return total_count

    def initialize_dp(self, n: int) -> List[defaultdict]:
        # Create a list of n defaultdict(int)
        return [defaultdict(int) for _ in range(n)]

    def calculate_difference(self, value_one: int, value_two: int) -> int:
        return value_one - value_two