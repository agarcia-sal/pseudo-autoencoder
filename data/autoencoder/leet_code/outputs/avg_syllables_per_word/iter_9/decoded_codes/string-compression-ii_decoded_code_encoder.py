class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        from functools import cache

        @cache
        def dp(i: int, k_remaining: int, prev_char: str, prev_count: int) -> int:
            if k_remaining < 0:
                return float('inf')
            if i == len(s):
                return 0

            curr_char = s[i]
            if curr_char == prev_char:
                increment = 1 if prev_count in {1, 9, 99} else 0
                return increment + dp(i + 1, k_remaining, prev_char, prev_count + 1)
            else:
                keep_cost = 1 + dp(i + 1, k_remaining, curr_char, 1)
                delete_cost = dp(i + 1, k_remaining - 1, prev_char, prev_count)
                return min(keep_cost, delete_cost)

        return dp(0, k, '', 0)