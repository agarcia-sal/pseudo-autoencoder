from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def countSubranges(self, nums1, nums2):
        n = len(nums1)
        dp = [defaultdict(int) for _ in range(n)]
        count = 0

        for i in range(n):
            dp[i][nums1[i]] += 1
            dp[i][-nums2[i]] += 1
            if i > 0:
                for balance, freq in dp[i-1].items():
                    temp_balance_plus = balance + nums1[i]
                    temp_balance_minus = balance - nums2[i]
                    dp[i][temp_balance_plus] = (dp[i][temp_balance_plus] + freq) % MOD
                    dp[i][temp_balance_minus] = (dp[i][temp_balance_minus] + freq) % MOD
            count = (count + dp[i][0]) % MOD
        return count