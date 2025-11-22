from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, list_of_numbers):
        index_map = {num: i for i, num in enumerate(list_of_numbers)}
        dp = {}
        max_len = 0

        for k in range(len(list_of_numbers)):
            for j in range(k):
                diff = list_of_numbers[k] - list_of_numbers[j]
                i = index_map.get(diff, -1)
                if i >= 0 and i < j:
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    if dp[(j, k)] > max_len:
                        max_len = dp[(j, k)]

        return max_len if max_len >= 3 else 0