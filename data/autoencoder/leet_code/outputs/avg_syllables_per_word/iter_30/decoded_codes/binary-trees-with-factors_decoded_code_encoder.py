class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 1
        arr.sort()
        dp = {num: 1 for num in arr}
        for i, num in enumerate(arr):
            for j in range(i):
                factor_candidate = arr[j]
                if num % factor_candidate == 0:
                    right_child = num // factor_candidate
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[factor_candidate] * dp[right_child]) % MOD
        total_trees = sum(dp.values())
        result = total_trees % MOD
        return result