from typing import List

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            row = pizza[i - 1]
            for j in range(1, n + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (1 if row[j - 1] == 'A' else 0)

        def apples(i1: int, j1: int, i2: int, j2: int) -> int:
            # Return number of apples in sub-pizza from (i1,j1) inclusive to (i2,j2) inclusive
            return s[i2+1][j2+1] - s[i2+1][j1] - s[i1][j2+1] + s[i1][j1]

        from functools import lru_cache
        @lru_cache(None)
        def dfs(i: int, j: int, remain: int) -> int:
            if remain == 0:
                return 1 if apples(i, j, m - 1, n - 1) > 0 else 0
            ans = 0
            for x in range(i + 1, m):
                if apples(x, j, m - 1, n - 1) > 0:
                    ans += dfs(x, j, remain - 1)
            for y in range(j + 1, n):
                if apples(i, y, m - 1, n - 1) > 0:
                    ans += dfs(i, y, remain - 1)
            return ans % mod

        return dfs(0, 0, k - 1)