from typing import List

class Solution:
    def maxChunksToSorted(self, arr_of_integers: List[int]) -> int:
        list_max_so_far = []
        current_max = arr_of_integers[0]
        for number in arr_of_integers:
            current_max = max(current_max, number)
            list_max_so_far.append(current_max)

        sorted_arr = sorted(arr_of_integers)
        chunks = 0
        max_chunk = float('-inf')
        for i in range(len(arr_of_integers)):
            max_chunk = max(max_chunk, arr_of_integers[i])
            if max_chunk == sorted_arr[i]:
                chunks += 1
        return chunks