from typing import List, Tuple

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_filtered: List[Tuple[str, int]] = []
        for index, character in enumerate(start):
            if character != 'X':
                start_filtered.append((character, index))

        end_filtered: List[Tuple[str, int]] = []
        for index, character in enumerate(end):
            if character != 'X':
                end_filtered.append((character, index))

        if len(start_filtered) != len(end_filtered):
            return False

        for (character1, index1), (character2, index2) in zip(start_filtered, end_filtered):
            if character1 != character2:
                return False
            if character1 == 'L' and index1 < index2:
                return False
            if character1 == 'R' and index1 > index2:
                return False

        return True