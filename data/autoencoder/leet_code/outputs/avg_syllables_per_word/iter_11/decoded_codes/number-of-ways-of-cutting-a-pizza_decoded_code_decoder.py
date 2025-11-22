from functools import cache

class Solution:
    def ways(self, pizza, k):
        mod = 10**9 + 7
        m = len(pizza)
        n = len(pizza[0])
        s = self.initialize_prefix_sum(m, n, pizza)

        @cache
        def dfs(i, j, k):
            if k == 0:
                if s[m][n] - s[i][n] - s[m][j] + s[i][j] > 0:
                    return 1
                else:
                    return 0

            ans = 0
            for x in range(i + 1, m):
                if s[x][n] - s[i][n] - s[x][j] + s[i][j] > 0:
                    ans += dfs(x, j, k - 1)

            for y in range(j + 1, n):
                if s[m][y] - s[i][y] - s[m][j] + s[i][j] > 0:
                    ans += dfs(i, y, k - 1)

            return ans % mod

        return dfs(0, 0, k - 1)

    def initialize_prefix_sum(self, m, n, pizza):
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(pizza, start=1):
            for j, c in enumerate(row, start=1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (1 if c == 'A' else 0)
        return s