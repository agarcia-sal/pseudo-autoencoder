class Solution:
    def maxSizeSlices(self, slices):
        n = len(slices) // 3

        def dp(slices, start, end, k):
            length = end - start + 1
            dp = [[0] * (k + 1) for _ in range(length + 2)]

            for i in range(length - 1, -1, -1):
                for j in range(1, k + 1):
                    pick = slices[start + i] + dp[i + 2][j - 1] if i + 2 <= length else slices[start + i]
                    skip = dp[i + 1][j] if i + 1 <= length else 0
                    dp[i][j] = max(pick, skip)
            return dp[0][k]

        case1 = dp(slices, 1, len(slices) - 1, n)
        case2 = dp(slices, 0, len(slices) - 2, n)
        return max(case1, case2)