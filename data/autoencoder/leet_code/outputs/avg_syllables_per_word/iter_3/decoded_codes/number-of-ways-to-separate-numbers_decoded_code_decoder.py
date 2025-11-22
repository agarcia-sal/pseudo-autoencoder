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
                memo[(index, prev_len)] = 0
                return 0

            for length in range(1, n - index + 1):
                if prev_len == 0:
                    count = (count + dp(index + length, length)) % MOD
                else:
                    prev_start = index - prev_len
                    prev_end = index
                    curr_num = num[index:index + length]
                    prev_num = num[prev_start:prev_end]

                    # Compare numbers by length and lex order for efficiency
                    if length > prev_len or (length == prev_len and curr_num >= prev_num):
                        count = (count + dp(index + length, length)) % MOD
                    else:
                        # Since curr_num is shorter or lex smaller, no need to continue with longer lengths
                        # Because longer lengths will be even larger than prev_len, so continue checking
                        pass

            memo[(index, prev_len)] = count
            return count

        return dp(0, 0)