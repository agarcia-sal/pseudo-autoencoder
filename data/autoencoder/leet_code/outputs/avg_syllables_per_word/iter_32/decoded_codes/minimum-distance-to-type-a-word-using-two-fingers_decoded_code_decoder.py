from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        def distance(c1: str | None, c2: str) -> int:
            if c1 is None:
                return 0
            # Compute row and column for c1 and c2
            # Keyboard is arranged in rows of 6 letters: A-F (0-5), G-L(6-11), ...
            idx1 = ord(c1) - ord('A')
            idx2 = ord(c2) - ord('A')
            x1, y1 = divmod(idx1, 6)
            x2, y2 = divmod(idx2, 6)
            return abs(x1 - x2) + abs(y1 - y2)

        n = len(word)

        @lru_cache(None)
        def dp(i: int, f1: str | None, f2: str | None) -> int:
            if i == n:
                return 0
            cur = word[i]
            # Move finger 1 to cur
            dist1 = distance(f1, cur) + dp(i + 1, cur, f2)
            # Move finger 2 to cur
            dist2 = distance(f2, cur) + dp(i + 1, f1, cur)
            return min(dist1, dist2)

        return dp(0, None, None)