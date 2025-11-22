class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = self.initialize_three_dimensional_list(n + 1, 2, 3)
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    # Ending with P (present)
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD

                    if j == 0:
                        # Inserting A (absent) if none before
                        dp[i][1][0] = (dp[i][1][0] + dp[i - 1][0][k]) % MOD

                    if k < 2:
                        # Ending with L (late), increase late count by one
                        dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i - 1][j][k]) % MOD

        result = 0
        for j in range(2):
            for k in range(3):
                result = (result + dp[n][j][k]) % MOD
        return result

    def initialize_three_dimensional_list(self, first_dimension: int, second_dimension: int, third_dimension: int):
        return [[[0] * third_dimension for _ in range(second_dimension)] for _ in range(first_dimension)]