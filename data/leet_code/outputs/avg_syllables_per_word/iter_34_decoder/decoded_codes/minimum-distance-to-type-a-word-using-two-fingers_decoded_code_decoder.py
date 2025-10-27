class Solution:
    def minimumDistance(self, word: str) -> int:
        def distance(c1, c2):
            if c1 is None:
                return 0
            x1, y1 = divmod(ord(c1) - ord('A'), 6)
            x2, y2 = divmod(ord(c2) - ord('A'), 6)
            return abs(x1 - x2) + abs(y1 - y2)

        from functools import lru_cache

        @lru_cache(None)
        def dp(i, f1, f2):
            if i == len(word):
                return 0
            c = word[i]
            d1 = distance(f1, c) + dp(i + 1, c, f2)
            d2 = distance(f2, c) + dp(i + 1, f1, c)
            return d1 if d1 < d2 else d2

        return dp(0, None, None)