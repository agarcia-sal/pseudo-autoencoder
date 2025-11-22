class Solution:
    def lenLongestFibSubseq(self, arr):
        index = {}
        for i, x in enumerate(arr):
            index[x] = i
        dp = {}
        max_length = 0

        for k in range(len(arr)):
            for j in range(k):
                i = index.get(arr[k] - arr[j], -1)
                if 0 <= i < j:
                    dp[j, k] = dp.get((i, j), 2) + 1
                    max_length = max(max_length, dp[j, k])

        return max_length if max_length >= 3 else 0