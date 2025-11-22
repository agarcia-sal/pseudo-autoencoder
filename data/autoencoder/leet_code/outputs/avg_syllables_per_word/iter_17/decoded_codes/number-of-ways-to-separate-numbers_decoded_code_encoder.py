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
            # Iterate over possible lengths of the current number substring
            for length in range(1, n - index + 1):
                if num[index] == '0':
                    break  # Leading zero invalidates any number starting here

                current_num = num[index:index + length]

                if prev_len == 0:
                    # No previous number to compare to
                    count += dp(index + length, length)
                    count %= MOD
                else:
                    prev_num = num[index - prev_len:index]
                    # Compare lengths and lex order:
                    # If length > prev_len, current_num > prev_num definitely,
                    # else if lengths equal, compare strings lex order.
                    if length > prev_len or (length == prev_len and current_num >= prev_num):
                        count += dp(index + length, length)
                        count %= MOD

            memo[(index, prev_len)] = count % MOD
            return memo[(index, prev_len)]

        return dp(0, 0)