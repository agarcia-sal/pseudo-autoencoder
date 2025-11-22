from functools import lru_cache
from math import ceil

class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0

        # Scale n as per problem statement with ceiling division by 25
        n = (n + 24) // 25

        @lru_cache(None)
        def dp(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            # Calculate probability as average of four serving options:
            # Each option decreases a and b by (4,0), (3,1), (2,2), (1,3) respectively.
            prob = 0.25 * (dp(a - 4, b) + dp(a - 3, b - 1) +
                           dp(a - 2, b - 2) + dp(a - 1, b - 3))
            return prob

        return dp(n, n)