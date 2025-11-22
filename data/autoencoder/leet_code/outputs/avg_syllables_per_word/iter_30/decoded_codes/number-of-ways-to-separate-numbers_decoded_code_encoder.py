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
            if num[index] == '0':
                # Leading zero invalidates number, no combinations
                memo[(index, prev_len)] = 0
                return 0

            count = 0
            max_len = n - index
            for length in range(1, max_len + 1):
                # current number substring
                current_num = num[index:index+length]

                if prev_len == 0:
                    # no previous number, so always valid
                    count += dp(index + length, length)
                    count %= MOD
                else:
                    # previous number substring
                    prev_num_start = index - prev_len
                    prev_num = num[prev_num_start:index]
                    # If lengths are equal or current number longer, compare lex order
                    # Since numbers have no leading zeros, lex comparison works for equal length
                    if length > prev_len:
                        count += dp(index + length, length)
                        count %= MOD
                    elif length == prev_len and current_num >= prev_num:
                        count += dp(index + length, length)
                        count %= MOD
                    # else current_num < prev_num -> skip
            memo[(index, prev_len)] = count
            return count

        return dp(0, 0)