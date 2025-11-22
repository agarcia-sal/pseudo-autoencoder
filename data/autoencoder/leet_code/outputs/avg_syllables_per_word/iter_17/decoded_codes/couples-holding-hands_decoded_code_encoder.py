from typing import List, Dict

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        position = self.create_position_dictionary(row)
        swaps = 0

        for index in range(0, len(row), 2):
            correct_pair = self.find_correct_pair(row[index])
            if row[index + 1] != correct_pair:
                swap_idx = self.find_swap_index(correct_pair, position)
                self.swap_elements(row, index + 1, swap_idx)
                self.update_position_dictionary(row, position, swap_idx)
                self.update_position_dictionary(row, position, index + 1)
                swaps += 1

        return swaps

    def create_position_dictionary(self, row: List[int]) -> Dict[int, int]:
        # Maps each person to their current index in the row
        return {person: idx for idx, person in enumerate(row)}

    def find_correct_pair(self, person: int) -> int:
        # Each couple consists of two consecutive integers: (0,1), (2,3), ...
        # Given a person, their partner is the person with the other parity in the pair
        if person % 2 == 0:
            return person + 1
        else:
            return person - 1

    def find_swap_index(self, correct_pair: int, position: Dict[int, int]) -> int:
        # Return the current index of the correct_pair in the row
        return position[correct_pair]

    def swap_elements(self, collection: List[int], index_one: int, index_two: int) -> None:
        collection[index_one], collection[index_two] = collection[index_two], collection[index_one]

    def update_position_dictionary(self, row: List[int], position: Dict[int, int], index: int) -> None:
        # Update the dictionary for the person at row[index]
        position[row[index]] = index