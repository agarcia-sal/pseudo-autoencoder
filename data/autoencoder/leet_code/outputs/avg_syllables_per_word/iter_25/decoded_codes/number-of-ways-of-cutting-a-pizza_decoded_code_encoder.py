class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0]) if pizza else 0

        # Prefix sum matrix s where s[i][j] is number of 'A's in submatrix pizza[:i][:j]
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(pizza, start=1):
            for j, c in enumerate(row, start=1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + (c == 'A')

        from functools import cache

        @cache
        def dfs(i: int, j: int, cuts: int) -> int:
            # Check if the current piece has any apples:
            total_apples = s[m][n] - s[i][n] - s[m][j] + s[i][j]
            if cuts == 0:
                return int(total_apples > 0)
            ans = 0

            # Horizontal cuts
            for x in range(i + 1, m):
                top_apples = s[x][n] - s[i][n] - s[x][j] + s[i][j]
                if top_apples > 0:
                    ans += dfs(x, j, cuts - 1)

            # Vertical cuts
            for y in range(j + 1, n):
                left_apples = s[m][y] - s[i][y] - s[m][j] + s[i][j]
                if left_apples > 0:
                    ans += dfs(i, y, cuts - 1)

            return ans % mod

        return dfs(0, 0, k - 1)