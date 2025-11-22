class Solution:
    def removeBoxes(self, boxes):
        def dp(l, r, k, memo):
            if l > r:
                return 0
            if (l, r, k) in memo:
                return memo[(l, r, k)]
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            res = dp(l, r - 1, 0, memo) + (k + 1) ** 2
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k + 1, memo) + dp(i + 1, r - 1, 0, memo))
            memo[(l, r, k)] = res
            return res

        return dp(0, len(boxes) - 1, 0, {})