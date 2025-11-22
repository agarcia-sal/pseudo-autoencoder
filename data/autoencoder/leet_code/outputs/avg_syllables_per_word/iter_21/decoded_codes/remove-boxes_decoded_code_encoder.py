class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        from functools import lru_cache

        n = len(boxes)

        # Use explicit memo dictionary because we have 3 parameters and k can grow dynamically.
        memo = {}

        def dp(l: int, r: int, k: int) -> int:
            if l > r:
                return 0
            if (l, r, k) in memo:
                return memo[(l, r, k)]

            # Optimization: increase k while boxes[r] == boxes[r - 1]
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1

            # Remove boxes[r] together with k boxes of the same color
            res = dp(l, r - 1, 0) + (k + 1) * (k + 1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))

            memo[(l, r, k)] = res
            return res

        return dp(0, n - 1, 0)