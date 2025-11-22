from collections import defaultdict
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        # dp[i]: dictionary mapping difference d -> count of arithmetic subsequences ending at index i with difference d
        dp = [defaultdict(int) for _ in range(n)]
        total_count = 0

        for i in range(n):
            for j in range(i):
                d = nums[i] - nums[j]
                count_j = dp[j].get(d, 0)
                dp[i][d] += count_j + 1
                total_count += count_j  # only count sequences of length >= 3

        return total_count