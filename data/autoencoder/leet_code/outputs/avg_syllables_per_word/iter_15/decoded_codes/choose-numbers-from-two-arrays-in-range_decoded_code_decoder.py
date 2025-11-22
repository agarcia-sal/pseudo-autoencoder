from collections import defaultdict
from typing import List

class Solution:
    MOD = 10**9 + 7

    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        count = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            dp[i][nums1[i]] = (dp[i][nums1[i]] + 1) % self.MOD
            dp[i][-nums2[i]] = (dp[i][-nums2[i]] + 1) % self.MOD
            if i > 0:
                for balance, freq in dp[i - 1].items():
                    sum_key = balance + nums1[i]
                    diff_key = balance - nums2[i]
                    dp[i][sum_key] = (dp[i][sum_key] + freq) % self.MOD
                    dp[i][diff_key] = (dp[i][diff_key] + freq) % self.MOD
            count = (count + dp[i].get(0, 0)) % self.MOD

        return count