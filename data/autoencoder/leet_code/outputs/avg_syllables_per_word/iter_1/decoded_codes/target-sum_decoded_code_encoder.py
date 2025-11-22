def findTargetSumWays(nums, target):
    def dfs(i, s, memo):
        if i == len(nums):
            return 1 if s == target else 0
        if (i, s) in memo:
            return memo[(i, s)]
        memo[(i, s)] = dfs(i+1, s+nums[i], memo) + dfs(i+1, s-nums[i], memo)
        return memo[(i, s)]
    return dfs(0, 0, {})