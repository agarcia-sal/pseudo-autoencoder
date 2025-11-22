from collections import Counter

def solve(nums):
    count = Counter(nums)
    unique = sorted(count.keys())

    dp = [0] * (len(unique) + 1)
    dp[1] = unique[0] * count[unique[0]]

    for i in range(2, len(unique) + 1):
        num = unique[i-1]
        if num == unique[i-2] + 1:
            dp[i] = max(dp[i-1], dp[i-2] + num * count[num])
        else:
            dp[i] = dp[i-1] + num * count[num]

    return dp[-1]