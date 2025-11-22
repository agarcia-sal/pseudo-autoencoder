from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def countSubranges(self, nums1List: list[int], nums2List: list[int]) -> int:
        n = len(nums1List)
        count = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            dp[i][nums1List[i]] += 1
            dp[i][-nums2List[i]] += 1

            if i > 0:
                for balance, freq in dp[i-1].items():
                    dp[i][balance + nums1List[i]] = (dp[i][balance + nums1List[i]] + freq) % MOD
                    dp[i][balance - nums2List[i]] = (dp[i][balance - nums2List[i]] + freq) % MOD

            count = (count + dp[i][0]) % MOD

        return count