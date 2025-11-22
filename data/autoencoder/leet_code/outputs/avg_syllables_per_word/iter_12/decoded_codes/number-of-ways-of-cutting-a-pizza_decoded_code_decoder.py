from functools import lru_cache

class Solution:
    def ways(self, pizza, k):
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])

        # Prefix sums: s[i][j] = number of apples in top-left submatrix (0,0) to (i-1,j-1)
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            row = pizza[i - 1]
            for j in range(1, n + 1):
                c = row[j - 1]
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (1 if c == 'A' else 0)

        # Check if there is at least one apple in pizza[i:m][j:n]
        def has_apple(i, j, x, y):
            return s[x][y] - s[i][y] - s[x][j] + s[i][j] > 0

        @lru_cache(None)
        def dfs(i, j, rem):
            if rem == 0:
                return 1 if has_apple(i, j, m, n) else 0
            ans = 0
            # Horizontal cuts
            for x in range(i + 1, m):
                if has_apple(i, j, x, n):
                    ans += dfs(x, j, rem - 1)
            # Vertical cuts
            for y in range(j + 1, n):
                if has_apple(i, j, m, y):
                    ans += dfs(i, y, rem - 1)
            return ans % mod

        return dfs(0, 0, k - 1)