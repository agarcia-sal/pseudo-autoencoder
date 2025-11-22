from collections import defaultdict

class Solution:
    def countSubranges(self, nums1, nums2):
        MOD = 10**9 + 7
        n = len(nums1)
        dp = [defaultdict(int) for _ in range(n)]
        count = 0

        for i in range(n):
            dp[i][nums1[i]] += 1
            dp[i][-nums2[i]] += 1

            if i > 0:
                prev_dp = dp[i - 1]
                current_dp = dp[i]
                for balance, freq in prev_dp.items():
                    new_balance_add = balance + nums1[i]
                    new_balance_sub = balance - nums2[i]
                    current_dp[new_balance_add] = (current_dp[new_balance_add] + freq) % MOD
                    current_dp[new_balance_sub] = (current_dp[new_balance_sub] + freq) % MOD

            count = (count + dp[i][0]) % MOD

        return count