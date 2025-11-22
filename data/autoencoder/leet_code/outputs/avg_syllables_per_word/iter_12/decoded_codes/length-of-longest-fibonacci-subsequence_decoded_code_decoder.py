from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr):
        index = {}
        for i, x in enumerate(arr):
            index[x] = i

        dp = {}
        max_length = 0

        for k in range(len(arr)):
            for j in range(k):
                required = arr[k] - arr[j]
                i = index.get(required, -1)
                if 0 <= i < j:
                    current_length = dp.get((i, j), 2)
                    dp[(j, k)] = current_length + 1
                    if dp[(j, k)] > max_length:
                        max_length = dp[(j, k)]

        return max_length if max_length >= 3 else 0