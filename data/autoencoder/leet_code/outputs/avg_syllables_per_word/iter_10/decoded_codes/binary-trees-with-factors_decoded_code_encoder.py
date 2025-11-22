class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        dp = {num: 1 for num in arr}
        for i, num in enumerate(arr):
            for j in range(i):
                potential_factor = arr[j]
                if num % potential_factor == 0:
                    right_child = num // potential_factor
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[potential_factor] * dp[right_child]) % MOD
        return sum(dp.values()) % MOD