class Solution:
    def numFactoredBinaryTrees(self, arr):
        MOD = 10**9 + 7
        arr.sort()
        dp = {x: 1 for x in arr}

        for i, num in enumerate(arr):
            for j in range(i):
                if num % arr[j] == 0:
                    right_child = num // arr[j]
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[arr[j]] * dp[right_child]) % MOD

        return sum(dp.values()) % MOD