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

            count = 0
            for length in range(1, n - index + 1):
                if num[index] == '0':
                    break
                current_num = num[index:index+length]
                if prev_len == 0:
                    count += dp(index + length, length)
                    count %= MOD
                else:
                    prev_start = index - prev_len
                    prev_num = num[prev_start:index]
                    if len(prev_num) == prev_len:
                        if length > prev_len or (length == prev_len and current_num >= prev_num):
                            count += dp(index + length, length)
                            count %= MOD

            memo[(index, prev_len)] = count
            return count

        return dp(0, 0)