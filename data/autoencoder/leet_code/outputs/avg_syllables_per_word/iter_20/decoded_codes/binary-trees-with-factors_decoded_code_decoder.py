class Solution:
    def numFactoredBinaryTrees(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        arr.sort()
        dp = {num: 1 for num in arr}

        for i in range(len(arr)):
            num = arr[i]
            for j in range(i):
                possible_factor = arr[j]
                if num % possible_factor == 0:
                    right_child = num // possible_factor
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[possible_factor] * dp[right_child]) % MOD

        return sum(dp.values()) % MOD