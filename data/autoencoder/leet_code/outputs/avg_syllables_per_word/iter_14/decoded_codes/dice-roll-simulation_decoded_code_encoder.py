class Solution:
    def dieSimulator(self, n: int, rollMax: [int]) -> int:
        MODULO = 10**9 + 7
        dp = [[[0] * (rollMax[j] + 1) for j in range(6)] for _ in range(n + 1)]

        # Base case: for i=1, one roll of each face with count=1
        for j in range(6):
            dp[1][j][1] = 1

        for i in range(2, n + 1):
            for j in range(6):
                max_roll_j = rollMax[j]
                for k in range(1, max_roll_j + 1):
                    if k > 1:
                        dp[i][j][k] = dp[i - 1][j][k - 1]
                    else:
                        temp_sum = 0
                        for x in range(6):
                            if x != j:
                                max_roll_x = rollMax[x]
                                for y in range(1, max_roll_x + 1):
                                    temp_sum += dp[i - 1][x][y]
                        dp[i][j][1] = temp_sum % MODULO

        total_ways = 0
        for j in range(6):
            max_roll_j = rollMax[j]
            for k in range(1, max_roll_j + 1):
                total_ways += dp[n][j][k]

        return total_ways % MODULO