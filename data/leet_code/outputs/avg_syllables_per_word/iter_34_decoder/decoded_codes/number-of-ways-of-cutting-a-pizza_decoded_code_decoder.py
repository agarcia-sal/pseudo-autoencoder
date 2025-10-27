from functools import cache

class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])

        # s[i][j] = number of apples in subrectangle ((i-1),(j-1)) down to (0,0)
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = (s[i-1][j] + s[i][j-1] - s[i-1][j-1] +
                           (1 if pizza[i - 1][j - 1] == 'A' else 0))

        def apples(r1: int, c1: int, r2: int, c2: int) -> int:
            # Returns number of apples in rectangle with top-left (r1,c1) and bottom-right (r2-1,c2-1)
            return s[r2][c2] - s[r1][c2] - s[r2][c1] + s[r1][c1]

        @cache
        def dfs(i: int, j: int, remain: int) -> int:
            if remain == 0:
                return 1 if apples(i, j, m, n) > 0 else 0
            ans = 0
            # Horizontal cuts
            for x in range(i + 1, m):
                if apples(i, j, x, n) > 0:
                    ans += dfs(x, j, remain - 1)
            # Vertical cuts
            for y in range(j + 1, n):
                if apples(i, j, m, y) > 0:
                    ans += dfs(i, y, remain - 1)
            return ans % mod

        return dfs(0, 0, k - 1)