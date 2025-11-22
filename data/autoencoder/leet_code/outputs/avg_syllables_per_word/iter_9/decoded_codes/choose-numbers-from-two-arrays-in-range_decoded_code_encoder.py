MOD = 10**9 + 7

class Solution:
    def countSubranges(self, nums1, nums2):
        n = len(nums1)
        count = 0
        dp = [dict() for _ in range(n)]

        for i in range(n):
            dp[i][nums1[i]] = dp[i].get(nums1[i], 0) + 1
            dp[i][-nums2[i]] = dp[i].get(-nums2[i], 0) + 1

            if i > 0:
                for balance, freq in dp[i-1].items():
                    dp[i][balance + nums1[i]] = (dp[i].get(balance + nums1[i], 0) + freq) % MOD
                    dp[i][balance - nums2[i]] = (dp[i].get(balance - nums2[i], 0) + freq) % MOD

            count = (count + dp[i].get(0, 0)) % MOD

        return count