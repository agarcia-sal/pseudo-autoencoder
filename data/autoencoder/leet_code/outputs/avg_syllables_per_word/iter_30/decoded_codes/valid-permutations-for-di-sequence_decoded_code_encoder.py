class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MODULO_VALUE = 10**9 + 1
        length_of_s = len(s)
        dp = [[0] * (length_of_s + 1) for _ in range(length_of_s + 1)]
        for j in range(length_of_s + 1):
            dp[0][j] = 1
        for i in range(1, length_of_s + 1):
            prefix_sum = 0
            if s[i - 1] == 'I':
                for j in range(length_of_s + 1 - i):
                    prefix_sum = (prefix_sum + dp[i - 1][j]) % MODULO_VALUE
                    dp[i][j] = prefix_sum
            else:
                for j in range(length_of_s - i, -1, -1):
                    prefix_sum = (prefix_sum + dp[i - 1][j + 1]) % MODULO_VALUE
                    dp[i][j] = prefix_sum
        result_sum = sum(dp[length_of_s]) % MODULO_VALUE
        return result_sum