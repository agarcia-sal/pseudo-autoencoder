from collections import defaultdict

class Solution:
    def countSubranges(self, nums1, nums2):
        mod = 10**9 + 7
        n = len(nums1)
        dp = [defaultdict(int) for _ in range(n)]
        count = 0

        for i in range(n):
            dp[i][nums1[i]] = (dp[i][nums1[i]] + 1) % mod
            dp[i][-nums2[i]] = (dp[i][-nums2[i]] + 1) % mod

            if i > 0:
                for balance, freq in dp[i-1].items():
                    dp[i][balance + nums1[i]] = (dp[i][balance + nums1[i]] + freq) % mod
                    dp[i][balance - nums2[i]] = (dp[i][balance - nums2[i]] + freq) % mod

            count = (count + dp[i][0]) % mod

        return count