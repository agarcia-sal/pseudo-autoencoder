from functools import lru_cache

class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)

        @lru_cache(None)
        def dp(index: int, prev_len: int) -> int:
            if index == n:
                return 1
            if num[index] == '0':
                return 0

            count = 0
            max_len = n - index
            for length in range(1, max_len + 1):
                # If prev_len == 0, no previous number to compare, so always valid
                if prev_len == 0:
                    count += dp(index + length, length)
                    count %= MOD
                else:
                    # To compare num[index:index+length] >= num[index-prev_len:index]
                    # if length > prev_len, new number is definitely bigger (as leading digit non-zero)
                    # if length < prev_len, new number is smaller
                    # if lengths equal, lex compare substrings
                    if length > prev_len:
                        count += dp(index + length, length)
                        count %= MOD
                    elif length == prev_len:
                        prev_num = num[index - prev_len : index]
                        curr_num = num[index : index + length]
                        if curr_num >= prev_num:
                            count += dp(index + length, length)
                            count %= MOD
                    # if length < prev_len: skip (current number smaller, invalid)
            return count % MOD

        return dp(0, 0)