class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = self.initialize_dp_table(n, k)
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                visible_case = dp[i - 1][j - 1]
                not_visible_case = (i - 1) * dp[i - 1][j]
                dp[i][j] = (visible_case + not_visible_case) % MOD
        return dp[n][k]

    def initialize_dp_table(self, n: int, k: int) -> list[list[int]]:
        return [[0] * (k + 1) for _ in range(n + 1)]