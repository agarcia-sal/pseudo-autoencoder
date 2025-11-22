from functools import lru_cache

class Solution:
    def removeBoxes(self, boxes):
        n = len(boxes)

        # Use lru_cache for memoization instead of manual dict for cleaner code
        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0
            # Optimize by extending the block of boxes[r] to the left with same boxes
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            # Remove boxes[r] and the k boxes to the right of it (all of the same value)
            res = dp(l, r - 1, 0) + (k + 1) * (k + 1)
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    # Try to merge boxes[i] with boxes[r], adding k + 1 boxes counted
                    res = max(res, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))
            return res

        return dp(0, n - 1, 0)