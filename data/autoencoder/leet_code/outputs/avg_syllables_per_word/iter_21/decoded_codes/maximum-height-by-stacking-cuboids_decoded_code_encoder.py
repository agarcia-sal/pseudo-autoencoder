from typing import List

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        # Sort each cuboid's dimensions to make them non-decreasing
        for cuboid in cuboids:
            cuboid.sort()
        # Sort all cuboids lexicographically
        cuboids.sort()

        n = len(cuboids)
        dp = [0] * n

        for i in range(n):
            dp[i] = cuboids[i][2]  # Height is the third dimension after sorting
            for j in range(i):
                if (cuboids[j][0] <= cuboids[i][0] and
                    cuboids[j][1] <= cuboids[i][1] and
                    cuboids[j][2] <= cuboids[i][2]):
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])

        return max(dp) if dp else 0