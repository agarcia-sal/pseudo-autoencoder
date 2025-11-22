from math import comb
from typing import List

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        n = sum(balls) // 2
        k = len(balls)

        # dfs(i, j, diff):
        # i: current color index
        # j: number of balls assigned to box 1 so far
        # diff: difference in distinct color counts (box1 - box2)
        def dfs(i: int, j: int, diff: int) -> int:
            if i >= k:
                # all colors processed
                return 1 if j == 0 and diff == 0 else 0
            if j < 0:
                # assigned too many balls to box 1
                return 0
            ans = 0
            total = balls[i]
            for x in range(total + 1):
                # For color i, we put x balls in box1, rest in box2
                if x == total:
                    y = 1   # box2 has zero balls of this color, box1 non-zero => distinct count diff +1
                elif x == 0:
                    y = -1  # box1 has zero balls of this color, box2 non-zero => distinct count diff -1
                else:
                    y = 0   # color present in both boxes, no diff change
                ways = comb(total, x)
                ans += dfs(i + 1, j - x, diff + y) * ways
            return ans

        total_ways = comb(sum(balls), n)
        return dfs(0, n, 0) / total_ways