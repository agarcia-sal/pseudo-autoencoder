from typing import List
from functools import lru_cache

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0]) if pizza else 0
        # Prefix sum array s with dimensions (m+1) x (n+1)
        # s[i][j] = number of 'A's in rectangle from top-left (0,0) to (i-1, j-1)
        s = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            row = pizza[i-1]
            for j in range(1, n+1):
                c = row[j-1]
                s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + (1 if c == 'A' else 0)

        def has_apple(r1: int, c1: int, r2: int, c2: int) -> bool:
            # Checks if sub-rectangle from (r1,c1) to (r2-1,c2-1) has at least one 'A'
            return (s[r2][c2] - s[r1][c2] - s[r2][c1] + s[r1][c1]) > 0

        @lru_cache(None)
        def dfs(i: int, j: int, cuts_left: int) -> int:
            if cuts_left == 0:
                return 1 if has_apple(i, j, m, n) else 0
            ans = 0
            # Horizontal cuts
            for x in range(i+1, m):
                if has_apple(i, j, x, n):
                    ans = (ans + dfs(x, j, cuts_left - 1)) % mod
            # Vertical cuts
            for y in range(j+1, n):
                if has_apple(i, j, m, y):
                    ans = (ans + dfs(i, y, cuts_left - 1)) % mod
            return ans

        return dfs(0, 0, k-1)