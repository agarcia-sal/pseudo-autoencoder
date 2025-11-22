from functools import lru_cache

class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        # Prefix sums: s[i][j] = number of 'A's in rectangle (0,0) to (i-1,j-1)
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + (1 if pizza[i-1][j-1] == 'A' else 0)

        @lru_cache(None)
        def dfs(i: int, j: int, rem: int) -> int:
            # If no more cuts left, check if remaining piece has at least one 'A'
            if rem == 0:
                return int(s[m][n] - s[i][n] - s[m][j] + s[i][j] > 0)
            ans = 0
            # horizontal cuts
            for x in range(i + 1, m):
                if s[x][n] - s[i][n] - s[x][j] + s[i][j] > 0:  # top piece has at least one A
                    ans += dfs(x, j, rem - 1)
            # vertical cuts
            for y in range(j + 1, n):
                if s[m][y] - s[i][y] - s[m][j] + s[i][j] > 0:  # left piece has at least one A
                    ans += dfs(i, y, rem - 1)
            return ans % mod

        return dfs(0, 0, k - 1)