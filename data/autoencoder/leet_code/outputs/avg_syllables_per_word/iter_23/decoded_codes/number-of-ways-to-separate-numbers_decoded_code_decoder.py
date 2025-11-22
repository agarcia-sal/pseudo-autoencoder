class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        memo = {}

        def dp(index: int, prev_len: int) -> int:
            if index == n:
                return 1
            if (index, prev_len) in memo:
                return memo[(index, prev_len)]

            count = 0
            if num[index] == '0':
                # Numbers cannot have leading zeros, so break early.
                memo[(index, prev_len)] = 0
                return 0

            for length in range(1, n - index + 1):
                if num[index] == '0':
                    # Leading zero check (redundant here due to earlier check)
                    break

                current_num = num[index:index + length]

                if prev_len == 0:
                    # No previous number, always can proceed
                    count += dp(index + length, length)
                    count %= MOD
                else:
                    prev_num = num[index - prev_len: index]

                    # Compare numerically without integer conversion by length and lex order
                    if length > prev_len:
                        # current_num longer than prev_num means current_num > prev_num
                        count += dp(index + length, length)
                        count %= MOD
                    elif length == prev_len:
                        # equal length, lex compare strings (digits)
                        if current_num >= prev_num:
                            count += dp(index + length, length)
                            count %= MOD
                    # If length < prev_len, current_num is smaller, so skip

            memo[(index, prev_len)] = count
            return count

        return dp(0, 0)