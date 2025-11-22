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
                current_num = num[index:index + length]

                if prev_len == 0 or current_num >= num[index - prev_len:index]:
                    count = (count + dp(index + length, length)) % MOD

            memo[(index, prev_len)] = count
            return count

        return dp(0, 0)