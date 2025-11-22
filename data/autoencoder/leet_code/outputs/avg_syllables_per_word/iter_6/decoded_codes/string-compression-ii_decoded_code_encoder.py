class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        from functools import cache
        n = len(s)

        @cache
        def dp(i: int, k: int, prev_char: str, prev_count: int) -> int:
            if k < 0:
                return float('inf')
            if i == n:
                return 0

            current_char = s[i]
            if current_char == prev_char:
                increment = 1 if prev_count in {1, 9, 99} else 0
                return increment + dp(i + 1, k, prev_char, prev_count + 1)
            else:
                keep = 1 + dp(i + 1, k, current_char, 1)
                delete = dp(i + 1, k - 1, prev_char, prev_count)
                return min(keep, delete)

        return dp(0, k, '', 0)