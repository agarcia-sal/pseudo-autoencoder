from functools import lru_cache

class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])

        # Prefix sum matrix s; s[i][j] = number of apples in submatrix from (0,0) to (i-1,j-1)
        s = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (1 if pizza[i - 1][j - 1] == 'A' else 0)

        def apples(i: int, j: int, x: int, y: int) -> int:
            # Number of apples in rectangle from (i,j) to (x-1,y-1)
            return s[x][y] - s[i][y] - s[x][j] + s[i][j]

        @lru_cache(None)
        def dfs(i: int, j: int, cuts: int) -> int:
            # If no more cuts, check if there is at least one apple in the remaining piece
            if cuts == 0:
                return 1 if apples(i, j, m, n) > 0 else 0

            ans = 0
            # Try horizontal cuts
            for x in range(i + 1, m):
                if apples(i, j, x, n) > 0:
                    ans += dfs(x, j, cuts - 1)
                    ans %= mod
            # Try vertical cuts
            for y in range(j + 1, n):
                if apples(i, j, m, y) > 0:
                    ans += dfs(i, y, cuts - 1)
                    ans %= mod
            return ans % mod

        return dfs(0, 0, k - 1)