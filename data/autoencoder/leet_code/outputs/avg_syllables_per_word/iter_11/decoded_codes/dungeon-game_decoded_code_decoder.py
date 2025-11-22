class Solution:
    def calculateMinimumHP(self, dungeon):
        m = len(dungeon)
        n = len(dungeon[0])
        dp = self.createDPTable(m + 1, n + 1)
        dp[m][n - 1] = 1
        dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_health = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = 1 if min_health < 1 else min_health
        return dp[0][0]

    def createDPTable(self, rows, columns):
        dp_table = []
        for _ in range(rows):
            dp_table.append([float('inf')] * columns)
        return dp_table