class Solution:
    def lenLongestFibSubseq(self, arr):
        index = {x: i for i, x in enumerate(arr)}
        dp = {}
        max_length = 0

        for k in range(len(arr)):
            for j in range(k):
                i = index.get(arr[k] - arr[j], -1)
                if i >= 0 and i < j:
                    current_length = dp.get((i, j), 2) + 1
                    dp[(j, k)] = current_length
                    if current_length > max_length:
                        max_length = current_length

        return max_length if max_length >= 3 else 0