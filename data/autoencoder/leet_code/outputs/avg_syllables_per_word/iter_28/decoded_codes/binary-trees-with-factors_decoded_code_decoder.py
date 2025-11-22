from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {x: 1 for x in arr}
        index_map = {x: i for i, x in enumerate(arr)}

        for i, num in enumerate(arr):
            for j in range(i):
                potential_factor = arr[j]
                if num % potential_factor == 0:
                    right_child = num // potential_factor
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[potential_factor] * dp[right_child]) % MOD

        return sum(dp.values()) % MOD