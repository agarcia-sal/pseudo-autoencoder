from collections import defaultdict
from typing import List

class Solution:
    def countSubranges(self, nums1: List[int], nums2: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums1)
        count = 0
        # dp[i]: defaultdict mapping balance to frequency of subranges ending at i with that balance
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            dp[i][nums1[i]] += 1
            dp[i][-nums2[i]] += 1

            if i > 0:
                for balance, freq in dp[i - 1].items():
                    dp[i][balance + nums1[i]] = (dp[i][balance + nums1[i]] + freq) % MOD
                    dp[i][balance - nums2[i]] = (dp[i][balance - nums2[i]] + freq) % MOD

            count = (count + dp[i].get(0, 0)) % MOD

        return count