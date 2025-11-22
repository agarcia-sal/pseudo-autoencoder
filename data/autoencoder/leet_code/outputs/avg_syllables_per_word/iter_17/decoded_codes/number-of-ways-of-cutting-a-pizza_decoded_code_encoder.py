class Solution:
    def ways(self, pizza: list[str], k: int) -> int:
        mod = 10**9 + 7
        m, n = len(pizza), len(pizza[0])
        s = self.create_prefix_sum_matrix(pizza, m, n)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i: int, j: int, k_left: int) -> int:
            if k_left == 0:
                # Check if the current piece has any apple using prefix sums
                return 1 if s[m][n] - s[i][n] - s[m][j] + s[i][j] > 0 else 0

            ans = 0
            # Try horizontal cuts
            for x in range(i + 1, m):
                if s[x][n] - s[i][n] - s[x][j] + s[i][j] > 0:
                    ans += dfs(x, j, k_left - 1)
            # Try vertical cuts
            for y in range(j + 1, n):
                if s[m][y] - s[i][y] - s[m][j] + s[i][j] > 0:
                    ans += dfs(i, y, k_left - 1)

            return ans % mod

        return dfs(0, 0, k - 1)

    def create_prefix_sum_matrix(self, pizza: list[str], m: int, n: int) -> list[list[int]]:
        s = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s[i][j] = s[i - 1][j] + s[i][j - 1] - s[i - 1][j - 1] + self.is_apple(pizza[i - 1][j - 1])
        return s

    def is_apple(self, character: str) -> int:
        return 1 if character == 'A' else 0