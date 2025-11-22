m, n = len(muls), len(nums)
dp = [0] * (m + 1)
for i in reversed(range(m)):
    new_dp = [0] * (m + 1)
    for left in range(i + 1):
        right = n - 1 - (i - left)
        new_dp[left] = max(muls[i] * nums[left] + dp[left + 1],
                           muls[i] * nums[right] + dp[left])
    dp = new_dp
return dp[0]