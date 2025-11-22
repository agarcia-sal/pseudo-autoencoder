from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def dfs(x: str, y: str) -> bool:
            if x == y:
                return True
            if sorted(x) != sorted(y):
                return False
            n = len(x)
            for i in range(1, n):
                # Case 1: No swap
                if dfs(x[:i], y[:i]) and dfs(x[i:], y[i:]):
                    return True
                # Case 2: Swap
                if dfs(x[:i], y[-i:]) and dfs(x[i:], y[:-i]):
                    return True
            return False

        return dfs(s1, s2)