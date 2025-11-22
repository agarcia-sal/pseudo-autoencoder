from collections import defaultdict

class Solution:
    def countSubranges(self, nums1: list[int], nums2: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums1)
        dp = [defaultdict(int) for _ in range(n)]
        count = 0

        for i in range(n):
            dp[i][nums1[i]] = (dp[i][nums1[i]] + 1) % MOD
            dp[i][-nums2[i]] = (dp[i][-nums2[i]] + 1) % MOD
            if i > 0:
                for balance, freq in dp[i-1].items():
                    key1 = balance + nums1[i]
                    dp[i][key1] = (dp[i][key1] + freq) % MOD

                    key2 = balance - nums2[i]
                    dp[i][key2] = (dp[i][key2] + freq) % MOD
            count = (count + dp[i].get(0, 0)) % MOD

        return count