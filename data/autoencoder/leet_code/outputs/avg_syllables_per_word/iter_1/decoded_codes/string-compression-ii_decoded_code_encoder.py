def get_min_length(s: str, k: int) -> int:
    from functools import lru_cache

    INF = float('inf')

    @lru_cache(None)
    def dp(i: int, k_left: int, pc: str, pcnt: int) -> int:
        if k_left < 0:
            return INF
        if i == len(s):
            return 0

        if s[i] == pc:
            inc = 1 if pcnt in {1, 9, 99} else 0
            return inc + dp(i+1, k_left, pc, pcnt+1)
        else:
            keep = 1 + dp(i+1, k_left, s[i], 1)
            delete = dp(i+1, k_left-1, pc, pcnt)
            return min(keep, delete)

    return dp(0, k, '', 0)