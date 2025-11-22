class Solution:
    def maximumScore(self, nums, multipliers):
        m = len(multipliers)
        n = len(nums)
        dp = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            new_dp = [0] * (m + 1)
            for left in range(i + 1):
                right = n - 1 - (i - left)
                mul = multipliers[i]
                new_dp[left] = max(
                    mul * nums[left] + dp[left + 1],
                    mul * nums[right] + dp[left]
                )
            dp = new_dp
        return dp[0]