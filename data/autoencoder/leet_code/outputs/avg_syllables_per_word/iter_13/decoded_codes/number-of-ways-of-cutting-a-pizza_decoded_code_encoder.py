class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]

        # Build prefix sum matrix s where s[i][j] = number of 'A's in the submatrix (0,0) to (i-1,j-1)
        for i, row in enumerate(pizza, 1):
            for j, c in enumerate(row, 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (1 if c == 'A' else 0)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, j: int, cuts_left: int) -> int:
            # Check if submatrix from (i,j) to bottom-right corner contains any 'A'
            def hasApple(x1: int, y1: int, x2: int, y2: int) -> bool:
                return (s[x2][y2] - s[x1][y2] - s[x2][y1] + s[x1][y1]) > 0

            if cuts_left == 0:
                return 1 if hasApple(i, j, m, n) else 0

            ans = 0
            # Horizontal cuts
            for x in range(i + 1, m):
                if hasApple(i, j, x, n):
                    ans += dfs(x, j, cuts_left - 1)
            # Vertical cuts
            for y in range(j + 1, n):
                if hasApple(i, j, m, y):
                    ans += dfs(i, y, cuts_left - 1)

            return ans % mod

        return dfs(0, 0, k - 1)