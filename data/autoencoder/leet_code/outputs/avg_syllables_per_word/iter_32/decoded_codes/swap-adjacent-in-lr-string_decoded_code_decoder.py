from typing import List, Tuple

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        filtered_start_list: List[Tuple[str, int]] = []
        filtered_end_list: List[Tuple[str, int]] = []

        for index_position, character_element in enumerate(start):
            if character_element != 'X':
                filtered_start_list.append((character_element, index_position))

        for index_position, character_element in enumerate(end):
            if character_element != 'X':
                filtered_end_list.append((character_element, index_position))

        if len(filtered_start_list) != len(filtered_end_list):
            return False

        for (character_one, index_one), (character_two, index_two) in zip(filtered_start_list, filtered_end_list):
            if character_one != character_two:
                return False
            if character_one == 'L' and index_one < index_two:
                return False
            if character_one == 'R' and index_one > index_two:
                return False

        return True