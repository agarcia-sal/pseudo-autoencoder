from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def countSubranges(self, nums1, nums2):
        n = len(nums1)
        dp = [defaultdict(int) for _ in range(n)]
        count = 0

        for index in range(n):
            dp[index][nums1[index]] += 1
            dp[index][-nums2[index]] += 1

            if index > 0:
                for balance, freq in dp[index - 1].items():
                    dp[index][balance + nums1[index]] = (dp[index][balance + nums1[index]] + freq) % MOD
                    dp[index][balance - nums2[index]] = (dp[index][balance - nums2[index]] + freq) % MOD

            count = (count + dp[index][0]) % MOD

        return count