from math import comb
from typing import List

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls) // 2
        k = len(balls)

        def dfs(i: int, j: int, diff: int) -> float:
            if i >= k:
                # When all ball colors have been distributed,
                # return 1 if j == 0 (all balls placed)
                # and diff == 0 (equal distinct counts), else 0
                return 1.0 if j == 0 and diff == 0 else 0.0
            if j < 0:
                # Impossible to place negative balls
                return 0.0

            ans = 0.0
            total_color = balls[i]
            for x in range(total_color + 1):
                # x: number of balls of color i in the first urn
                # y tracks how distinct ball counts difference changes:
                # +1 if all balls of this color go to first urn (contributes one distinct color)
                # -1 if no balls go to first urn (all go to second urn)
                # 0 otherwise
                if x == total_color:
                    y = 1
                elif x == 0:
                    y = -1
                else:
                    y = 0

                # Choose x balls from total_color and recurse
                ways = comb(total_color, x)
                ans += dfs(i + 1, j - x, diff + y) * ways

            return ans

        total_ways = comb(sum(balls), n)
        return dfs(0, n, 0) / total_ways if total_ways > 0 else 0.0