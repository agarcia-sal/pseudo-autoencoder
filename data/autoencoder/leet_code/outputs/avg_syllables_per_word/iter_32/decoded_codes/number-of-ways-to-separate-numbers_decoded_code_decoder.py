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
                # Leading zero invalidates any number starting here
                return 0

            count = 0
            max_len = n - index
            for length in range(1, max_len + 1):
                current_num = num[index:index+length]
                if prev_len == 0:
                    # No previous number, so accept any current number
                    count += dp(index + length, length)
                    count %= MOD
                else:
                    # Compare current_num to previous number of length prev_len
                    prev_start = index - prev_len
                    prev_num = num[prev_start:prev_start + prev_len]
                    if length < prev_len:
                        # Current number shorter than previous - can't be greater or equal
                        continue
                    elif length > prev_len:
                        # Current number longer than previous - definitely greater
                        count += dp(index + length, length)
                        count %= MOD
                    else:
                        # Same length - lexicographic compare
                        if current_num >= prev_num:
                            count += dp(index + length, length)
                            count %= MOD
            return count % MOD

        return dp(0, 0)