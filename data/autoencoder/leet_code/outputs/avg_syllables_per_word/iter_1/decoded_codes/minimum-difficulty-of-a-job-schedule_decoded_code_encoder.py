from math import inf

def minDifficulty(jobDifficulty, d):
    n = len(jobDifficulty)
    if n < d:
        return -1

    from functools import lru_cache

    @lru_cache(None)
    def dp(i, day):
        if day == 1:
            return max(jobDifficulty[i:])
        min_diff = inf
        current_max = 0
        for j in range(i, n - day + 1):
            current_max = max(current_max, jobDifficulty[j])
            min_diff = min(min_diff, current_max + dp(j + 1, day - 1))
        return min_diff

    return dp(0, d)