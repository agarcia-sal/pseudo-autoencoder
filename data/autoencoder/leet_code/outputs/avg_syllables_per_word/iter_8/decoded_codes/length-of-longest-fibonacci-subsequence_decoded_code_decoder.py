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
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    if dp[(j, k)] > max_length:
                        max_length = dp[(j, k)]

        if max_length >= 3:
            return max_length
        else:
            return 0