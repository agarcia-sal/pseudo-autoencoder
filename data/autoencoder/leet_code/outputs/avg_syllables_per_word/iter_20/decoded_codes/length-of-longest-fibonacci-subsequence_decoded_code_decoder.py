from typing import List, Dict, Tuple
from collections import defaultdict

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index: Dict[int, int] = {x: i for i, x in enumerate(arr)}
        dp: Dict[Tuple[int, int], int] = defaultdict(int)
        max_length = 0
        n = len(arr)

        for k in range(n):
            for j in range(k):
                i = index.get(arr[k] - arr[j], -1)
                if 0 <= i < j:
                    dp[(j, k)] = dp.get((i, j), 2) + 1
                    if dp[(j, k)] > max_length:
                        max_length = dp[(j, k)]

        return max_length if max_length >= 3 else 0