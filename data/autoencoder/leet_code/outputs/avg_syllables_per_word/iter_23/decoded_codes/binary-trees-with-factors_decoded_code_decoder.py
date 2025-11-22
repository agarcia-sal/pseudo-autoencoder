from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {x:1 for x in arr}
        index_map = {x:i for i, x in enumerate(arr)}

        for i, num in enumerate(arr):
            for j in range(i):
                if num % arr[j] == 0:
                    right_child = num // arr[j]
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[arr[j]] * dp[right_child]) % MOD

        total = sum(dp.values())
        return total % MOD