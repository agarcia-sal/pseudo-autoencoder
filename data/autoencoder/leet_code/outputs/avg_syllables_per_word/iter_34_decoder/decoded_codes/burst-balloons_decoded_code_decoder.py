class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                for k in range(i + 1, j):
                    coins = nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]
                    if dp[i][j] < coins:
                        dp[i][j] = coins
        return dp[0][n - 1]