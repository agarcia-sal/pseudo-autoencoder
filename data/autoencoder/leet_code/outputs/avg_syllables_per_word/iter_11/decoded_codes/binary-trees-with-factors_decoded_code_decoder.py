class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        dp = {num: 1 for num in arr}
        index_map = {num: i for i, num in enumerate(arr)}

        for i in range(len(arr)):
            num = arr[i]
            for j in range(i):
                factor_candidate = arr[j]
                if num % factor_candidate == 0:
                    right_child = num // factor_candidate
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[factor_candidate] * dp[right_child]) % MOD

        total_trees = sum(dp.values()) % MOD
        return total_trees