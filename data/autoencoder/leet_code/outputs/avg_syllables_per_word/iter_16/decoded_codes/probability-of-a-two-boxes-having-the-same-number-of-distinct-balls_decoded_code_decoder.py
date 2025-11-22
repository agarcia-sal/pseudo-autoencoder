from math import comb

class Solution:
    def getProbability(self, balls):
        n = sum(balls) // 2
        k = len(balls)

        from functools import lru_cache

        @lru_cache(None)
        def dfs(i, j, diff):
            if i >= k:
                return 1 if j == 0 and diff == 0 else 0
            if j < 0:
                return 0
            ans = 0
            ball_count = balls[i]
            for x in range(ball_count + 1):
                if x == ball_count:
                    y = 1
                elif x == 0:
                    y = -1
                else:
                    y = 0
                ans += dfs(i + 1, j - x, diff + y) * comb(ball_count, x)
            return ans

        total = dfs(0, n, 0)
        return total / comb(sum(balls), n * 2)