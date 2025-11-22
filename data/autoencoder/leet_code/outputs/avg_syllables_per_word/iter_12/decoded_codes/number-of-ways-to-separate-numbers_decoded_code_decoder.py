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

            if num[index] == '0':  # leading zero is invalid, no numbers start with zero
                memo[(index, prev_len)] = 0
                return 0

            count = 0
            for length in range(1, n - index + 1):
                current_num = num[index:index + length]
                if prev_len == 0:
                    count += dp(index + length, length)
                else:
                    prev_num = num[index - prev_len:index]
                    # Check if current_num >= prev_num as numbers (strings of digits)
                    # Lengths can differ, so first compare length, then lex order
                    if length > prev_len or (length == prev_len and current_num >= prev_num):
                        count += dp(index + length, length)
                count %= MOD

            memo[(index, prev_len)] = count
            return count

        return dp(0, 0)