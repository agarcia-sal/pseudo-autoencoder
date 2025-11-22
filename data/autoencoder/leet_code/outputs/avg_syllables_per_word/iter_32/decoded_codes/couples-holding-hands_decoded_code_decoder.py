from typing import List, Dict

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        position: Dict[int, int] = {}
        for index, person in enumerate(row):
            position[person] = index

        swaps = 0
        length_of_row = len(row)
        i = 0

        while i < length_of_row:
            current_person = row[i]
            next_person = row[i + 1]
            # Determine the correct pair for current_person:
            # If even, pair is current_person + 1, else current_person - 1
            correct_pair = current_person + 1 if current_person % 2 == 0 else current_person - 1

            if next_person != correct_pair:
                swap_idx = position[correct_pair]
                # Swap next_person and the correct_pair in the row
                row[i + 1], row[swap_idx] = row[swap_idx], row[i + 1]
                # Update positions after swap
                position[correct_pair] = i + 1
                position[next_person] = swap_idx
                swaps += 1
            i += 2

        return swaps