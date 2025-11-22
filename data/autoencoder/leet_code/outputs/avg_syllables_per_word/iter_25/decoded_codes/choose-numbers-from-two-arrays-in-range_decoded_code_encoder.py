from collections import defaultdict

class Solution:
    def countSubranges(self, nums1: list[int], nums2: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums1)
        count = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            dp[i][nums1[i]] += 1
            dp[i][-nums2[i]] += 1

            if i > 0:
                for balance, freq in dp[i-1].items():
                    dp[i][balance + nums1[i]] = (dp[i][balance + nums1[i]] + freq) % MOD
                    dp[i][balance - nums2[i]] = (dp[i][balance - nums2[i]] + freq) % MOD

            count = (count + dp[i][0]) % MOD

        return count