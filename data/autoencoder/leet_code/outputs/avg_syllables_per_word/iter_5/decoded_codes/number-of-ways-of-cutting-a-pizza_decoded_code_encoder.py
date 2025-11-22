class Solution:
    def ways(self, pizza, k):
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + (1 if pizza[i-1][j-1] == 'A' else 0)

        from functools import cache

        @cache
        def dfs(i, j, cuts):
            if cuts == 0:
                return 1 if s[m][n] - s[i][n] - s[m][j] + s[i][j] > 0 else 0
            ans = 0
            for x in range(i + 1, m):
                if s[x][n] - s[i][n] - s[x][j] + s[i][j] > 0:
                    ans = (ans + dfs(x, j, cuts - 1)) % mod
            for y in range(j + 1, n):
                if s[m][y] - s[i][y] - s[m][j] + s[i][j] > 0:
                    ans = (ans + dfs(i, y, cuts - 1)) % mod
            return ans

        return dfs(0, 0, k - 1)