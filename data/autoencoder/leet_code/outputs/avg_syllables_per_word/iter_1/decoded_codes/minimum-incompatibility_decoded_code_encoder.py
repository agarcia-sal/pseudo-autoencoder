from collections import Counter

def min_incompatibility(nums, k):
    n = len(nums)
    sz = n // k
    if any(count > k for count in Counter(nums).values()):
        return -1

    subset_incomp = {}
    for mask in range(1 << n):
        if bin(mask).count('1') == sz:
            elems = [nums[i] for i in range(n) if mask & (1 << i)]
            if len(set(elems)) == sz:
                subset_incomp[mask] = max(elems) - min(elems)

    INF = float('inf')
    dp = [INF] * (1 << n)
    dp[0] = 0

    for mask in range(1 << n):
        if bin(mask).count('1') % sz != 0:
            continue
        for sub in subset_incomp:
            if (mask & sub) == sub:
                dp[mask] = min(dp[mask], dp[mask ^ sub] + subset_incomp[sub])

    return dp[(1 << n) - 1] if dp[(1 << n) - 1] != INF else -1