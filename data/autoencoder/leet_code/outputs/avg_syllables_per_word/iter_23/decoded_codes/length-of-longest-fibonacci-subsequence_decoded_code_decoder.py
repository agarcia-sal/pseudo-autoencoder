from typing import List, Dict, Tuple

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index: Dict[int, int] = {}
        for i, x in enumerate(arr):
            index[x] = i

        dp: Dict[Tuple[int, int], int] = {}
        max_length = 0

        for k in range(len(arr)):
            for j in range(k):
                diff = arr[k] - arr[j]
                i = index.get(diff, -1)
                if 0 <= i < j:
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    if dp[(j, k)] > max_length:
                        max_length = dp[(j, k)]

        return max_length if max_length >= 3 else 0