from typing import List

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_filtered = [(c, i) for i, c in enumerate(start) if c != 'X']
        end_filtered = [(c, i) for i, c in enumerate(end) if c != 'X']

        if len(start_filtered) != len(end_filtered):
            return False

        for (char_one, index_one), (char_two, index_two) in zip(start_filtered, end_filtered):
            if char_one != char_two:
                return False
            if char_one == 'L' and index_one < index_two:
                return False
            if char_one == 'R' and index_one > index_two:
                return False

        return True