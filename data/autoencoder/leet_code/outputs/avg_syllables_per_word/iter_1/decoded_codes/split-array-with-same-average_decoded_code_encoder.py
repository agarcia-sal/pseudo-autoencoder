def split_array_same_average(nums):
    n = len(nums)
    S = sum(nums)
    if n == 1:
        return False
    dp = [set() for _ in range(n // 2 + 1)]
    dp[0] = {0}
    for x in nums:
        for i in range(n // 2, 0, -1):
            for s in dp[i - 1]:
                ns = s + x
                if ns * n == i * S:
                    return True
                dp[i].add(ns)
    return False