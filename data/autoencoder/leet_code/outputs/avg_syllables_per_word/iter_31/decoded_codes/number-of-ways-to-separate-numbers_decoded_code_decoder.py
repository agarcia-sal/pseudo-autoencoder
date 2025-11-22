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
                if prev_len == 0:
                    # no previous number, just choose any valid starting number
                    count += dp(index + length, length)
                    count %= MOD
                else:
                    if length > prev_len:
                        # current number longer than previous number: always larger
                        count += dp(index + length, length)
                        count %= MOD
                    elif length == prev_len:
                        # compare substrings lex to decide if current >= previous number
                        prev_start = index - prev_len
                        prev_num = num[prev_start:prev_start+prev_len]
                        curr_num = num[index:index+length]
                        if curr_num >= prev_num:
                            count += dp(index + length, length)
                            count %= MOD
                    else:
                        # current number shorter than previous number -> smaller, skip
                        continue

            return count % MOD

        return dp(0, 0)