class Solution:
    def numFactoredBinaryTrees(self, arr):
        MODULO = 10**9 + 7
        arr.sort()
        dp = {num: 1 for num in arr}

        for i, num in enumerate(arr):
            for j in range(i):
                if num % arr[j] == 0:
                    right_child = num // arr[j]
                    if right_child in dp:
                        dp[num] = (dp[num] + dp[arr[j]] * dp[right_child]) % MODULO

        total_count = sum(dp.values()) % MODULO
        return total_count