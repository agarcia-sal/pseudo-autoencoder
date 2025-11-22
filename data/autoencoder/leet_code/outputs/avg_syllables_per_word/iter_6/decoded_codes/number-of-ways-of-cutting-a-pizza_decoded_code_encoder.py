class Solution:
    def ways(self, pizza, k):
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])

        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (pizza[i - 1][j - 1] == 'A')

        def apples(i, j, x, y):
            return s[x][y] - s[i][y] - s[x][j] + s[i][j]

        from functools import cache

        @cache
        def dfs(i, j, cuts):
            if cuts == 0:
                return 1 if apples(i, j, m, n) > 0 else 0

            ans = 0
            for x in range(i + 1, m):
                if apples(i, j, x, n) > 0:
                    ans += dfs(x, j, cuts - 1)
            for y in range(j + 1, n):
                if apples(i, j, m, y) > 0:
                    ans += dfs(i, y, cuts - 1)
            return ans % mod

        return dfs(0, 0, k - 1)