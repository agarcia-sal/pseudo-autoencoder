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
                return 0

            count = 0
            max_len = n - index
            for length in range(1, max_len + 1):
                if num[index] == '0':
                    break
                # If prev_len == 0, no previous number to compare, so proceed
                # Else compare current substring with previous substring of length prev_len
                if prev_len == 0:
                    count += dp(index + length, length)
                    count %= MOD
                else:
                    prev_start = index - prev_len
                    prev_sub = num[prev_start:prev_start + prev_len]
                    curr_sub = num[index:index + length]
                    if length < prev_len or (length == prev_len and curr_sub >= prev_sub):
                        count += dp(index + length, length)
                        count %= MOD
                    elif length > prev_len:
                        # If current length is greater than prev_len, current number is definitely greater
                        count += dp(index + length, length)
                        count %= MOD
                    else:
                        # current substring smaller than previous number, skip
                        pass

            memo[(index, prev_len)] = count % MOD
            return memo[(index, prev_len)]

        return dp(0, 0)