class Solution:
    def largestSumOfAverages(self, nums, k):
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        def average(i, j):
            return (prefix_sum[j + 1] - prefix_sum[i]) / (j - i + 1)

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][1] = average(i, n - 1)

        for i in range(n - 1, -1, -1):
            for partitions in range(2, k + 1):
                for j in range(i + 1, n):
                    value = dp[j][partitions - 1] + average(i, j - 1)
                    if value > dp[i][partitions]:
                        dp[i][partitions] = value

        return dp[0][k]