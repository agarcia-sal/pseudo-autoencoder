from functools import lru_cache

class Solution:
    def ways(self, pizza, k):
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        # prefix sums of apples: s[i][j] = number of apples in submatrix pizza[:i, :j]
        s = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + (1 if pizza[i-1][j-1] == 'A' else 0)

        def has_apple(i, j, x, y):
            # return True if submatrix pizza[i:x, j:y] has at least one 'A'
            return s[x][y] - s[i][y] - s[x][j] + s[i][j] > 0

        @lru_cache(None)
        def dfs(i, j, k):
            if k == 0:
                # if remaining piece has at least one apple, return 1 else 0
                return 1 if has_apple(i, j, m, n) else 0
            ans = 0
            # horizontal cuts
            for x in range(i+1, m):
                if has_apple(i, j, x, n):
                    ans = (ans + dfs(x, j, k - 1)) % mod
            # vertical cuts
            for y in range(j+1, n):
                if has_apple(i, j, m, y):
                    ans = (ans + dfs(i, y, k - 1)) % mod
            return ans % mod

        return dfs(0, 0, k-1)