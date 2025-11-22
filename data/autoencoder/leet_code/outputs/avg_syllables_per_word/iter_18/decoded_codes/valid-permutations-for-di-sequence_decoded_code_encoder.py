class Solution:
    def numPermsDISequence(self, s: str) -> int:
        MODULO = 10**9 + 7
        n = len(s)
        dp_table = [[0] * (n + 1) for _ in range(n + 1)]

        for j in range(n + 1):
            dp_table[0][j] = 1

        for i in range(1, n + 1):
            cumulative_prefix_sum = 0
            if s[i - 1] == 'I':
                for j in range(n + 1 - i):
                    cumulative_prefix_sum = (cumulative_prefix_sum + dp_table[i - 1][j]) % MODULO
                    dp_table[i][j] = cumulative_prefix_sum
            else:
                for j in range(n - i, -1, -1):
                    cumulative_prefix_sum = (cumulative_prefix_sum + dp_table[i - 1][j + 1]) % MODULO
                    dp_table[i][j] = cumulative_prefix_sum

        result_sum = sum(dp_table[n]) % MODULO
        return result_sum