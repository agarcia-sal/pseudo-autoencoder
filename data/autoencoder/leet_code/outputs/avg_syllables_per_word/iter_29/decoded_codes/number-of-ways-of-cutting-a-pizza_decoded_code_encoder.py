class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])

        # s[i][j] = number of apples in subrectangle from (i,j) to bottom-right corner
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                s[i][j] = (s[i + 1][j] + s[i][j + 1] - s[i + 1][j + 1] +
                           (1 if pizza[i][j] == 'A' else 0))

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, j: int, cuts_left: int) -> int:
            if cuts_left == 0:
                # If there's at least one apple in subrectangle starting at (i,j)
                return 1 if s[i][j] > 0 else 0

            ans = 0
            # Horizontal cuts
            for x in range(i + 1, m):
                # If lower piece has apple(s), we can cut horizontally at row x
                if s[i][j] - s[x][j] > 0:
                    ans += dfs(x, j, cuts_left - 1)

            # Vertical cuts
            for y in range(j + 1, n):
                # If right piece has apple(s), we can cut vertically at column y
                if s[i][j] - s[i][y] > 0:
                    ans += dfs(i, y, cuts_left - 1)

            return ans % mod

        return dfs(0, 0, k - 1)