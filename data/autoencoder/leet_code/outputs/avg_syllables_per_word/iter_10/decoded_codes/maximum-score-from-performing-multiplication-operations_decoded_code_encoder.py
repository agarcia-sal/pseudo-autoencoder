class Solution:
    def maximumScore(self, nums, multipliers):
        m, n = len(multipliers), len(nums)
        dp = [0] * (m + 1)
        for i in range(m - 1, -1, -1):
            new_dp = [0] * (m + 1)
            mul = multipliers[i]
            for left in range(i + 1):
                right = n - 1 - (i - left)
                val_left = mul * nums[left] + dp[left + 1]
                val_right = mul * nums[right] + dp[left]
                new_dp[left] = val_left if val_left > val_right else val_right
            dp = new_dp
        return dp[0]