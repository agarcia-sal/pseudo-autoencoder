from functools import cache
from typing import List

class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        mod = 10**9 + 7
        m = len(pizza)
        n = len(pizza[0])

        # Prefix sums of apples count in sub-rectangle from (0,0) to (i,j)
        # s[i][j] = number of apples in pizza[0:i][0:j]
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(pizza, start=1):
            for j, c in enumerate(row, start=1):
                s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + (1 if c == 'A' else 0)

        @cache
        def dfs(i: int, j: int, cuts_left: int) -> int:
            # Check if there is at least one apple in the current rectangle pizza[i:m][j:n]
            total_apples = s[m][n] - s[i][n] - s[m][j] + s[i][j]
            if cuts_left == 0:
                return int(total_apples > 0)

            ans = 0
            # Try vertical cuts
            for x in range(i + 1, m):
                # Check if the upper part pizza[i:x][j:n] contains at least one apple
                upper_apples = s[x][n] - s[i][n] - s[x][j] + s[i][j]
                if upper_apples > 0:
                    ans += dfs(x, j, cuts_left - 1)

            # Try horizontal cuts
            for y in range(j + 1, n):
                # Check if the left part pizza[i:m][j:y] contains at least one apple
                left_apples = s[m][y] - s[i][y] - s[m][j] + s[i][j]
                if left_apples > 0:
                    ans += dfs(i, y, cuts_left - 1)

            return ans % mod

        return dfs(0, 0, k - 1)