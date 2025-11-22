class Solution:
    def removeBoxes(self, boxes):
        from functools import lru_cache

        n = len(boxes)

        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0

            # Optimize by merging boxes of the same color at the end
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1

            res = dp(l, r - 1, 0) + (k + 1) * (k + 1)

            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))

            return res

        return dp(0, n - 1, 0)