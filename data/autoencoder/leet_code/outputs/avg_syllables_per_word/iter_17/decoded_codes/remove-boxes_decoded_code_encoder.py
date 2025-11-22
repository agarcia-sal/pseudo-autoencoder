class Solution:
    def removeBoxes(self, boxes: list[int]) -> int:
        from functools import lru_cache

        n = len(boxes)

        # Use memoization for dp function instead of passing dictionary explicitly
        @lru_cache(None)
        def dp(left: int, right: int, k: int) -> int:
            if left > right:
                return 0

            # Optimize by merging continuous same-valued boxes at the right end
            while right > left and boxes[right] == boxes[right - 1]:
                right -= 1
                k += 1

            # Remove the rightmost group of boxes plus merge with others if same color found earlier
            res = dp(left, right - 1, 0) + (k + 1) * (k + 1)

            for i in range(left, right):
                if boxes[i] == boxes[right]:
                    res = max(res, dp(left, i, k + 1) + dp(i + 1, right - 1, 0))
            return res

        return dp(0, n - 1, 0)