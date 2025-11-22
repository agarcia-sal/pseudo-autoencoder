from collections import defaultdict

class Solution:
    def countSubranges(self, nums1: list[int], nums2: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums1)
        count = 0
        # dp[i]: dictionary mapping balance -> frequency for subranges ending at i
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(n):
            dp[i][nums1[i]] += 1
            dp[i][-nums2[i]] += 1

            if i > 0:
                for balance, freq in dp[i - 1].items():
                    new_key_addition = balance + nums1[i]
                    dp[i][new_key_addition] = (dp[i][new_key_addition] + freq) % MOD

                    new_key_subtraction = balance - nums2[i]
                    dp[i][new_key_subtraction] = (dp[i][new_key_subtraction] + freq) % MOD

            count = (count + dp[i].get(0, 0)) % MOD

        return count