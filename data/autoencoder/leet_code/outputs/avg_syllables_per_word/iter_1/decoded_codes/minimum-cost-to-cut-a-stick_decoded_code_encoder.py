def min_cost(n, cuts):
    sort_cuts = sorted(cuts + [0, n])

    from functools import lru_cache

    @lru_cache(None)
    def dp(left, right):
        if right - left <= 1:
            return 0
        return min(
            sort_cuts[right] - sort_cuts[left] + dp(left, i) + dp(i, right)
            for i in range(left + 1, right)
        )

    return dp(0, len(sort_cuts) - 1)