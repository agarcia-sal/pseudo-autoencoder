from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {x: 1 for x in arr}  # Each element itself forms one tree

        for i in range(len(arr)):
            num = arr[i]
            for j in range(i):
                potential_factor = arr[j]
                if num % potential_factor == 0:
                    right_child = num // potential_factor
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[potential_factor] * dp[right_child]) % MOD

        total = sum(dp.values()) % MOD
        return total