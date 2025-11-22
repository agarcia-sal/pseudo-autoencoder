class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:
            return 1.0

        n = (n + 24) // 25
        memo = {}

        def dp(a: int, b: int) -> float:
            if (a, b) in memo:
                return memo[(a, b)]

            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0

            probability = 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )
            memo[(a, b)] = probability
            return probability

        return dp(n, n)