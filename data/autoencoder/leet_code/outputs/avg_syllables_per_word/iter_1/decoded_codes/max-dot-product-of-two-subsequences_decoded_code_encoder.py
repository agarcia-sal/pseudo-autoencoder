def max_product_subsequence(nums1, nums2):
    m, n = len(nums1), len(nums2)
    dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cur = nums1[i - 1] * nums2[j - 1]
            dp[i][j] = max(cur, dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + cur)
    return dp[m][n]