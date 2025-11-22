def solution(word):
    from functools import lru_cache

    def dist(c1, c2):
        if c1 is None:
            return 0
        return abs((ord(c1) - 65) // 6 - (ord(c2) - 65) // 6) + abs((ord(c1) - 65) % 6 - (ord(c2) - 65) % 6)

    @lru_cache(None)
    def dp(i, f1, f2):
        if i == len(word):
            return 0
        c = word[i]
        return min(dist(f1, c) + dp(i + 1, c, f2), dist(f2, c) + dp(i + 1, f1, c))

    return dp(0, None, None)