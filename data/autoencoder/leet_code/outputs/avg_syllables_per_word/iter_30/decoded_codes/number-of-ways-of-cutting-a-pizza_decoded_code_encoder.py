from functools import lru_cache

class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])

        # Prefix sums for apples count in subrectangles
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + (1 if pizza[i-1][j-1] == 'A' else 0)

        def apples(i1: int, j1: int, i2: int, j2: int) -> int:
            # Return number of apples in subrectangle [(i1,j1), (i2-1,j2-1)]
            return s[i2][j2] - s[i1][j2] - s[i2][j1] + s[i1][j1]

        @lru_cache(None)
        def dfs(i: int, j: int, pieces_left: int) -> int:
            if pieces_left == 0:
                return 1 if apples(i, j, m, n) > 0 else 0
            ans = 0
            # horizontal cuts
            for x in range(i + 1, m):
                if apples(i, j, x, n) > 0:
                    ans += dfs(x, j, pieces_left - 1)
            # vertical cuts
            for y in range(j + 1, n):
                if apples(i, j, m, y) > 0:
                    ans += dfs(i, y, pieces_left - 1)
            return ans % mod

        return dfs(0, 0, k - 1)