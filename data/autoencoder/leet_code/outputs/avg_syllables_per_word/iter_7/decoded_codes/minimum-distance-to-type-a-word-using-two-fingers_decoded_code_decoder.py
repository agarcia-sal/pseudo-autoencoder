from functools import cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        def distance(c1: str | None, c2: str) -> int:
            if c1 is None:
                return 0
            x1, y1 = divmod(ord(c1) - ord('A'), 6)
            x2, y2 = divmod(ord(c2) - ord('A'), 6)
            return abs(x1 - x2) + abs(y1 - y2)

        @cache
        def dp(i: int, f1: str | None, f2: str | None) -> int:
            if i == len(word):
                return 0
            c = word[i]
            d1 = distance(f1, c) + dp(i + 1, c, f2)
            d2 = distance(f2, c) + dp(i + 1, f1, c)
            return min(d1, d2)

        return dp(0, None, None)