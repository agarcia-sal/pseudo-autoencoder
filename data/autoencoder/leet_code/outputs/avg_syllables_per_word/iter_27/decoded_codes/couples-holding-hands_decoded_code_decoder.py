from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        position = {}
        for i, person in enumerate(row):
            position[person] = i

        swaps = 0
        n = len(row)
        for i in range(0, n, 2):
            correct_pair = row[i] ^ 1
            if row[i + 1] != correct_pair:
                swap_idx = position[correct_pair]

                # swap row[i+1] and row[swap_idx]
                temp = row[i + 1]
                row[i + 1] = row[swap_idx]
                row[swap_idx] = temp

                # update positions after swap
                position[row[swap_idx]] = swap_idx
                position[row[i + 1]] = i + 1

                swaps += 1

        return swaps