from functools import lru_cache

class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])

        # Prefix sums matrix s, size (m+1) x (n+1)
        s = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            row = pizza[i - 1]
            for j in range(1, n + 1):
                c = row[j - 1]
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (1 if c == 'A' else 0)

        def has_apple(x1: int, y1: int, x2: int, y2: int) -> bool:
            # Return True if submatrix from (x1,y1) to (x2-1,y2-1) contains at least one 'A'
            # Note: s uses 1-based indexing so parameters must add 1 for boundaries
            # But indices passed here are 0-based start, exclusive end
            return s[x2][y2] - s[x1][y2] - s[x2][y1] + s[x1][y1] > 0

        @lru_cache(None)
        def dfs(i: int, j: int, cuts_remaining: int) -> int:
            if cuts_remaining == 0:
                # Check if the sub-pizza from (i,j) to (m,n) has at least one apple
                return 1 if has_apple(i, j, m, n) else 0

            ans = 0
            # horizontal cuts
            for x in range(i + 1, m):
                if has_apple(i, j, x, n):
                    ans += dfs(x, j, cuts_remaining - 1)
            # vertical cuts
            for y in range(j + 1, n):
                if has_apple(i, j, m, y):
                    ans += dfs(i, y, cuts_remaining - 1)

            return ans % mod

        return dfs(0, 0, k - 1)