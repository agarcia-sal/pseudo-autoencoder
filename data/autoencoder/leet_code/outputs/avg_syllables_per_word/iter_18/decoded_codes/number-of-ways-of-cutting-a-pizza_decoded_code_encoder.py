class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        # Prefix sums array to count number of 'A's in submatrices
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            row = pizza[i - 1]
            for j in range(1, n + 1):
                c = row[j - 1]
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (1 if c == 'A' else 0)

        from functools import lru_cache

        def has_apple(i1: int, j1: int, i2: int, j2: int) -> bool:
            # Checks if there is at least one 'A' in the submatrix pizza[i1:i2, j1:j2]
            return (s[i2][j2] - s[i1][j2] - s[i2][j1] + s[i1][j1]) > 0

        @lru_cache(None)
        def dfs(i: int, j: int, cuts_left: int) -> int:
            if cuts_left == 0:
                # If no cuts left, check if current piece has at least one apple
                return 1 if has_apple(i, j, m, n) else 0
            ans = 0
            # Try horizontal cuts
            for x in range(i + 1, m):
                if has_apple(i, j, x, n):
                    ans += dfs(x, j, cuts_left - 1)
            # Try vertical cuts
            for y in range(j + 1, n):
                if has_apple(i, j, m, y):
                    ans += dfs(i, y, cuts_left - 1)
            return ans % mod

        return dfs(0, 0, k - 1)