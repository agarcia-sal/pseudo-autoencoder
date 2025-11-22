class Solution:
    def numberOfCombinations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        memo = {}

        def dp(index, prev_len):
            if index == n:
                return 1
            if (index, prev_len) in memo:
                return memo[(index, prev_len)]

            if num[index] == '0':
                memo[(index, prev_len)] = 0
                return 0

            count = 0
            max_len = n - index
            for length in range(1, max_len + 1):
                if num[index] == '0':
                    break
                if prev_len == 0:
                    count += dp(index + length, length)
                else:
                    prev_start = index - prev_len
                    prev_sub = num[prev_start:index]
                    curr_sub = num[index:index + length]
                    if length > prev_len or (length == prev_len and curr_sub >= prev_sub):
                        count += dp(index + length, length)
                count %= MOD

            memo[(index, prev_len)] = count
            return count

        return dp(0, 0)