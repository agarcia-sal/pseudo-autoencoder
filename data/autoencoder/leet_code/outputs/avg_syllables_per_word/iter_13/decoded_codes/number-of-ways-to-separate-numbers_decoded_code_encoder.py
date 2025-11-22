class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        memo = {}

        def dp(index: int, prev_len: int) -> int:
            if index == n:
                return 1

            key = (index, prev_len)
            if key in memo:
                return memo[key]

            if num[index] == '0':
                memo[key] = 0
                return 0

            count = 0
            max_len = n - index
            for length in range(1, max_len + 1):
                current_num = num[index:index+length]

                if prev_len == 0:
                    # No previous substring to compare
                    count = (count + dp(index + length, length)) % MOD
                else:
                    prev_start = index - prev_len
                    prev_end = index
                    prev_num = num[prev_start:prev_end]
                    if length > prev_len:
                        # If current length is greater than prev length, automatically valid
                        count = (count + dp(index + length, length)) % MOD
                    elif length == prev_len and current_num >= prev_num:
                        # Equal length, lex compare substrings
                        count = (count + dp(index + length, length)) % MOD
                    # If current length < prev_len, can't be >= prev_num of longer length, so skip

            memo[key] = count
            return count

        return dp(0, 0)