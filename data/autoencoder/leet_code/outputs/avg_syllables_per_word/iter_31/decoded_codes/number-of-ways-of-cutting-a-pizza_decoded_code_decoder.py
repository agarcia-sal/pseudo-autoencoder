from functools import lru_cache

class Solution:
    def ways(self, pizza, k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0]) if pizza else 0

        # Prefix sum array s of size (m+1) x (n+1), 
        # where s[i][j] = number of 'A' in pizza[:i, :j]
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            row = pizza[i - 1]
            for j in range(1, n + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (1 if row[j - 1] == 'A' else 0)

        def apples_in_region(r1, c1, r2, c2):
            # returns number of 'A' in pizza[r1:r2, c1:c2]
            return s[r2][c2] - s[r1][c2] - s[r2][c1] + s[r1][c1]

        @lru_cache(None)
        def dfs(i, j, cuts_remaining):
            if cuts_remaining == 0:
                # If the remaining piece has at least one apple
                return 1 if apples_in_region(i, j, m, n) > 0 else 0

            ans = 0
            # horizontal cuts
            for x in range(i+1, m):
                if apples_in_region(i, j, x, n) > 0:
                    ans += dfs(x, j, cuts_remaining - 1)
                    if ans >= mod:
                        ans -= mod
            # vertical cuts
            for y in range(j+1, n):
                if apples_in_region(i, j, m, y) > 0:
                    ans += dfs(i, y, cuts_remaining - 1)
                    if ans >= mod:
                        ans -= mod
            return ans % mod

        return dfs(0, 0, k - 1)