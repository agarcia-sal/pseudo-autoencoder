def rob(nums):
    def rob_linear(h):
        if not h:
            return 0
        if len(h) == 1:
            return h[0]
        dp = [0] * len(h)
        dp[0], dp[1] = h[0], max(h[0], h[1])
        for i in range(2, len(h)):
            dp[i] = max(dp[i-1], dp[i-2] + h[i])
        return dp[-1]

    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))