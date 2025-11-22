def stoneGameV(stoneValue):
    n = len(stoneValue)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]

    def get_sum(l, r):
        return prefix_sum[r + 1] - prefix_sum[l]

    from functools import lru_cache

    @lru_cache(None)
    def dp(l, r):
        if l == r:
            return 0
        max_score = 0
        for i in range(l, r):
            left_sum = get_sum(l, i)
            right_sum = get_sum(i + 1, r)
            if left_sum < right_sum:
                max_score = max(max_score, left_sum + dp(l, i))
            elif left_sum > right_sum:
                max_score = max(max_score, right_sum + dp(i + 1, r))
            else:
                max_score = max(max_score, left_sum + dp(l, i), right_sum + dp(i + 1, r))
        return max_score

    return dp(0, n - 1)