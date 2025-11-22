from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        def average(i: int, j: int) -> float:
            return (prefix_sum[j + 1] - prefix_sum[i]) / (j - i + 1)

        dp = [[0.0] * (k + 1) for _ in range(n + 1)]

        for i in range(n):
            dp[i][1] = average(i, n - 1)

        for i in range(n - 1, -1, -1):
            for partitions in range(2, k + 1):
                for j in range(i + 1, n):
                    dp[i][partitions] = max(
                        dp[i][partitions], dp[j][partitions - 1] + average(i, j - 1)
                    )

        return dp[0][k]