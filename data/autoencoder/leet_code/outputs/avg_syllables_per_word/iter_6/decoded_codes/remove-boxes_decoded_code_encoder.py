class Solution:
    def removeBoxes(self, boxes):
        from functools import lru_cache

        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            res = dp(l, r - 1, 0) + (k + 1) ** 2
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))
            return res

        return dp(0, len(boxes) - 1, 0)