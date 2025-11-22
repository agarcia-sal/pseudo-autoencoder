from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        def average(i: int, j: int) -> float:
            numerator = prefix_sum[j + 1] - prefix_sum[i]
            denominator = j - i + 1
            return numerator / denominator

        dp = [[0.0] * (k + 1) for _ in range(n + 1)]

        # Base case: when only one partition (k=1), the average is over the segment [i..n-1]
        for i in range(n):
            dp[i][1] = average(i, n - 1)

        # Fill dp for partitions from 2 to k
        for i in range(n - 1, -1, -1):
            for partitions in range(2, k + 1):
                max_val = 0.0
                # j must be at least i+1 to ensure a non-empty first partition
                for j in range(i + 1, n):
                    candidate = dp[j][partitions - 1] + average(i, j - 1)
                    if candidate > max_val:
                        max_val = candidate
                dp[i][partitions] = max_val

        return dp[0][k]