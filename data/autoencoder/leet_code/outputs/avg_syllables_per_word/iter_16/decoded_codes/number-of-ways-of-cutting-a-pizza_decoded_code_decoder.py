class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]

        # Prefix sum to count apples in sub-rectangle
        for i, row in enumerate(pizza, 1):
            for j, c in enumerate(row, 1):
                s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + (c == 'A')

        from functools import cache

        @cache
        def dfs(i: int, j: int, k: int) -> int:
            if k == 0:
                return int(s[m][n] - s[i][n] - s[m][j] + s[i][j] > 0)

            ans = 0
            # horizontal cuts
            for x in range(i + 1, m):
                if s[x][n] - s[i][n] - s[x][j] + s[i][j] > 0:
                    ans += dfs(x, j, k - 1)
            # vertical cuts
            for y in range(j + 1, n):
                if s[m][y] - s[i][y] - s[m][j] + s[i][j] > 0:
                    ans += dfs(i, y, k - 1)

            return ans % mod

        return dfs(0, 0, k - 1)