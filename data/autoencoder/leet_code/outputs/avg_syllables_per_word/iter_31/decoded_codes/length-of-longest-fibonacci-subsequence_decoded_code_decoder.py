from typing import List, Dict, Tuple

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        index: Dict[int, int] = {x: i for i, x in enumerate(arr)}
        dp: Dict[Tuple[int, int], int] = {}
        max_length = 0

        for k in range(len(arr)):
            for j in range(k):
                diff = arr[k] - arr[j]
                i = index.get(diff, -1)
                if 0 <= i < j:
                    base_length = dp.get((i, j), 2)
                    curr_length = base_length + 1
                    dp[(j, k)] = curr_length
                    if curr_length > max_length:
                        max_length = curr_length

        return max_length if max_length >= 3 else 0