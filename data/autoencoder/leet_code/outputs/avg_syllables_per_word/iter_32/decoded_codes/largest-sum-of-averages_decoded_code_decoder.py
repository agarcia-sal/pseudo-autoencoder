from typing import List

class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # Calculate average of subarray nums[i:j+1]
        def average(i: int, j: int) -> float:
            return (prefix_sum[j + 1] - prefix_sum[i]) / (j - i + 1)

        dp = [[0.0] * (k + 1) for _ in range(n + 1)]

        # Base case: one partition -> average of nums[i:n]
        for i in range(n):
            dp[i][1] = average(i, n - 1)

        # Fill dp for partitions from 2 to k
        for i in range(n - 1, -1, -1):
            for partitions in range(2, k + 1):
                # Early pruning: cannot partition if remaining length < partitions
                if n - i < partitions:
                    continue
                for j in range(i + 1, n):
                    current = dp[j][partitions - 1] + average(i, j - 1)
                    if current > dp[i][partitions]:
                        dp[i][partitions] = current

        return dp[0][k]