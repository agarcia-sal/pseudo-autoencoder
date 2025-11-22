from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MODULO = 10**9 + 7
        arr.sort()
        dp = {num: 1 for num in arr}  # each number itself forms one tree

        for i in range(len(arr)):
            num = arr[i]
            for j in range(i):
                factor_candidate = arr[j]
                if num % factor_candidate == 0:
                    right_child = num // factor_candidate
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[factor_candidate] * dp[right_child]) % MODULO

        total_trees = sum(dp.values()) % MODULO
        return total_trees