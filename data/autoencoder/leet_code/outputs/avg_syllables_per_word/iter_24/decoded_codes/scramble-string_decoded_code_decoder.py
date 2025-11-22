from functools import lru_cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def helper(a: str, b: str) -> bool:
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False
            n = len(a)
            for i in range(1, n):
                if helper(a[:i], b[:i]) and helper(a[i:], b[i:]):
                    return True
                if helper(a[:i], b[-i:]) and helper(a[i:], b[:-i]):
                    return True
            return False
        return helper(s1, s2)