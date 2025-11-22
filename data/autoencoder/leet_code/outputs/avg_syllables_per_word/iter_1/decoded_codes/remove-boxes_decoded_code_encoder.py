def removeBoxes(boxes):
    def dp(l, r, k, m):
        if l > r:
            return 0
        if (l, r, k) in m:
            return m[(l, r, k)]

        while r > l and boxes[r] == boxes[r - 1]:
            r -= 1
            k += 1

        res = dp(l, r - 1, 0, m) + (k + 1) ** 2
        for i in range(l, r):
            if boxes[i] == boxes[r]:
                res = max(res, dp(l, i, k + 1, m) + dp(i + 1, r - 1, 0, m))

        m[(l, r, k)] = res
        return res

    return dp(0, len(boxes) - 1, 0, {})