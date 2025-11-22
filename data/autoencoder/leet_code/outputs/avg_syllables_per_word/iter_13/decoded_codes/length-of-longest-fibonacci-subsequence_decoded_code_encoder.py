class Solution:
    def lenLongestFibSubseq(self, arr):
        index = {x: i for i, x in enumerate(arr)}
        dp = {}
        max_length = 0
        for k in range(len(arr)):
            for j in range(k):
                diff = arr[k] - arr[j]
                i = index.get(diff, -1)
                if 0 <= i < j:
                    prev_len = dp.get((i, j), 2)
                    dp[(j, k)] = prev_len + 1
                    if dp[(j, k)] > max_length:
                        max_length = dp[(j, k)]
        return max_length if max_length >= 3 else 0