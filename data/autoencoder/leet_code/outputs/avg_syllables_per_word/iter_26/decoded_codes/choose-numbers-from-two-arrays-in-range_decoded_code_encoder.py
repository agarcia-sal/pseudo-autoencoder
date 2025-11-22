from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def countSubranges(self, nums1, nums2):
        n = len(nums1)
        count = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            dp[i][nums1[i]] += 1
            dp[i][-nums2[i]] += 1
            if i > 0:
                for key, val in dp[i - 1].items():
                    new_balance_plus = key + nums1[i]
                    new_balance_minus = key - nums2[i]

                    dp[i][new_balance_plus] = (dp[i][new_balance_plus] + val) % MOD
                    dp[i][new_balance_minus] = (dp[i][new_balance_minus] + val) % MOD

            count = (count + dp[i][0]) % MOD

        return count