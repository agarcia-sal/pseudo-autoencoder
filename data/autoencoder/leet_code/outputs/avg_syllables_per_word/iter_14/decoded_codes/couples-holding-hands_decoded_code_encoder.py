from typing import List

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        position = self.helper_create_position_mapping(row)
        swaps = 0

        for index in range(0, len(row), 2):
            correct_pair = self.helper_find_correct_pair(row[index])
            if row[index + 1] != correct_pair:
                swap_idx = position[correct_pair]

                self.helper_swap_positions(row, index + 1, swap_idx)

                # Update the positions in the mapping after the swap
                position[row[swap_idx]] = swap_idx
                position[row[index + 1]] = index + 1

                swaps += 1

        return swaps

    def helper_create_position_mapping(self, row: List[int]) -> dict[int, int]:
        mapping = {}
        for index, person in enumerate(row):
            mapping[person] = index
        return mapping

    def helper_find_correct_pair(self, person: int) -> int:
        return person ^ 1

    def helper_swap_positions(self, row: List[int], position_one: int, position_two: int) -> None:
        row[position_one], row[position_two] = row[position_two], row[position_one]