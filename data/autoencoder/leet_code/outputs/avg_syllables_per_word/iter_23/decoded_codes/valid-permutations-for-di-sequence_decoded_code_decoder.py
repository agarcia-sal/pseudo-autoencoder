class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MODULO = 10**9 + 7
        length_of_s = len(s)
        dp = [[0] * (length_of_s + 1) for _ in range(length_of_s + 1)]

        for j in range(length_of_s + 1):
            dp[0][j] = 1

        for i in range(1, length_of_s + 1):
            prefix_sum = 0
            if s[i - 1] == 'I':
                for j in range(length_of_s - i + 1):
                    prefix_sum = (prefix_sum + dp[i - 1][j]) % MODULO
                    dp[i][j] = prefix_sum
            else:
                for j in range(length_of_s - i, -1, -1):
                    prefix_sum = (prefix_sum + dp[i - 1][j + 1]) % MODULO
                    dp[i][j] = prefix_sum

        total_valid_permutations = sum(dp[length_of_s]) % MODULO
        return total_valid_permutations