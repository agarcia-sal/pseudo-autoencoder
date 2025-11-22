from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_so_far = []
        current_max = arr[0] if arr else None
        for num in arr:
            if current_max is None or current_max < num:
                current_max = num
            max_so_far.append(current_max)

        sorted_arr = sorted(arr)
        chunks = 0
        max_chunk = float('-inf')

        for i in range(len(arr)):
            if max_chunk < max_so_far[i]:
                max_chunk = max_so_far[i]
            if max_chunk == sorted_arr[i]:
                chunks += 1

        return chunks