class Solution:
    def lenLongestFibSubseq(self, arr):
        index = {x: i for i, x in enumerate(arr)}
        dp = {}
        max_length = 0
        for k in range(len(arr)):
            for j in range(k):
                i = index.get(arr[k] - arr[j], -1)
                if i >= 0 and i < j:
                    dp[j, k] = dp.get((i, j), 2) + 1
                    if dp[j, k] > max_length:
                        max_length = dp[j, k]
        return max_length if max_length >= 3 else 0