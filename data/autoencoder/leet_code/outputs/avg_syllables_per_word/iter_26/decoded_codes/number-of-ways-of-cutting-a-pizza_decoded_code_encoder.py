from functools import lru_cache

class Solution:
    def ways(self, pizza: [str], k: int) -> int:
        mod = 10**9 + 7
        m = len(pizza)
        n = len(pizza[0])

        # Prefix sums matrix s with dimensions (m+1) x (n+1)
        s = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            row = pizza[i - 1]
            for j in range(1, n + 1):
                character = row[j - 1]
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (1 if character == 'A' else 0)

        def has_apple(x1: int, y1: int, x2: int, y2: int) -> bool:
            # Returns True if the sub-rectangle from (x1,y1) to (x2,y2) contains at least one 'A'
            return s[x2][y2] - s[x1][y2] - s[x2][y1] + s[x1][y1] > 0

        @lru_cache(None)
        def dfs(i: int, j: int, cuts: int) -> int:
            if cuts == 0:
                # Check if remaining piece has at least one apple
                return 1 if has_apple(i, j, m, n) else 0

            ans = 0
            # Horizontal cuts
            for x in range(i + 1, m):
                if has_apple(i, j, x, n):
                    ans += dfs(x, j, cuts - 1)
            # Vertical cuts
            for y in range(j + 1, n):
                if has_apple(i, j, m, y):
                    ans += dfs(i, y, cuts - 1)
            return ans % mod

        return dfs(0, 0, k - 1)