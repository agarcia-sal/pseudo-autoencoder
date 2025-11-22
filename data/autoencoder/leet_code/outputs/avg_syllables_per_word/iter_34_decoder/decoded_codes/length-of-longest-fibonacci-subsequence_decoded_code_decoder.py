class Solution:
    def lenLongestFibSubseq(self, arr):
        index = {x: i for i, x in enumerate(arr)}
        dp = {}
        max_length = 0

        for k in range(len(arr)):
            for j in range(k):
                i = index.get(arr[k] - arr[j], -1)
                if i >= 0 and i < j:
                    prev_len = dp.get((i, j), 2)
                    curr_len = prev_len + 1
                    dp[(j, k)] = curr_len
                    if curr_len > max_length:
                        max_length = curr_len

        return max_length if max_length >= 3 else 0