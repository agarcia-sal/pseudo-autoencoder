from collections import defaultdict

class Solution:
    MODULO = 10**9 + 7

    def countSubranges(self, nums1, nums2):
        n = len(nums1)
        count = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            dp[i][nums1[i]] = (dp[i][nums1[i]] + 1) % self.MODULO
            dp[i][-nums2[i]] = (dp[i][-nums2[i]] + 1) % self.MODULO

            if i > 0:
                for balance, freq in dp[i-1].items():
                    sum_key = balance + nums1[i]
                    dp[i][sum_key] = (dp[i][sum_key] + freq) % self.MODULO

                    diff_key = balance - nums2[i]
                    dp[i][diff_key] = (dp[i][diff_key] + freq) % self.MODULO

            current_zero_count = dp[i].get(0, 0)
            count = (count + current_zero_count) % self.MODULO

        return count