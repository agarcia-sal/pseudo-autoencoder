from functools import lru_cache

class Solution:
    def ways(self, pizza, k):
        mod = 10**9 + 7
        m = len(pizza)
        n = len(pizza[0])

        # prefix sum s[i][j] = number of apples in pizza[:i, :j]
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            row = pizza[i - 1]
            for j in range(1, n + 1):
                c = row[j - 1]
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (1 if c == 'A' else 0)

        def has_apple(i1, j1, i2, j2):
            # check if there is at least one apple in pizza[i1:i2, j1:j2]
            return (s[i2][j2] - s[i1][j2] - s[i2][j1] + s[i1][j1]) > 0

        @lru_cache(None)
        def dfs(i, j, pieces_left):
            if pieces_left == 0:
                return 1 if has_apple(i, j, m, n) else 0

            ans = 0
            # horizontal cuts
            for x in range(i + 1, m):
                if has_apple(i, j, x, n):
                    ans = (ans + dfs(x, j, pieces_left - 1)) % mod
            # vertical cuts
            for y in range(j + 1, n):
                if has_apple(i, j, m, y):
                    ans = (ans + dfs(i, y, pieces_left - 1)) % mod

            return ans

        return dfs(0, 0, k - 1)