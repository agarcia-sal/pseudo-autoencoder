from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = 0
        chunks = 0
        for index, val in enumerate(arr):
            if val > max_so_far:
                max_so_far = val
            if max_so_far == index:
                chunks += 1
        return chunks