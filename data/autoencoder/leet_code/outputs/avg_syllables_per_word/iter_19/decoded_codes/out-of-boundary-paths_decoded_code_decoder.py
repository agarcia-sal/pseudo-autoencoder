class Solution:
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        MOD = 10**9 + 7
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        # dp[k][i][j]: number of ways to move out of boundary from position (i,j) with k moves
        dp = [[[0]*n for _ in range(m)] for _ in range(maxMove+1)]

        for k in range(1, maxMove+1):
            for i in range(m):
                for j in range(n):
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if ni < 0 or ni >= m or nj < 0 or nj >= n:
                            dp[k][i][j] = (dp[k][i][j] + 1) % MOD
                        else:
                            dp[k][i][j] = (dp[k][i][j] + dp[k-1][ni][nj]) % MOD

        return dp[maxMove][startRow][startColumn]