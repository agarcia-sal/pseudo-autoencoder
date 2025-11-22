from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {}
        for num in arr:
            dp[num] = 1

        for i in range(len(arr)):
            num = arr[i]
            for j in range(i):
                potential_factor = arr[j]
                if num % potential_factor == 0:
                    right_child = num // potential_factor
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[potential_factor] * dp[right_child]) % MOD

        total_trees = sum(dp.values()) % MOD
        return total_trees