class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        dp = {x: 1 for x in arr}

        for i in range(len(arr)):
            num = arr[i]
            for j in range(i):
                factor = arr[j]
                if num % factor == 0:
                    right_child = num // factor
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[factor] * dp[right_child]) % MOD

        return sum(dp.values()) % MOD