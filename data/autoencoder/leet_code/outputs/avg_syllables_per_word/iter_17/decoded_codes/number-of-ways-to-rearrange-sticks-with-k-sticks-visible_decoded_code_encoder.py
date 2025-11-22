class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MODULO = 10**9 + 7
        dp_table = [[0] * (k + 1) for _ in range(n + 1)]
        dp_table[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                dp_table[i][j] = (dp_table[i - 1][j - 1] + (i - 1) * dp_table[i - 1][j]) % MODULO
        return dp_table[n][k]