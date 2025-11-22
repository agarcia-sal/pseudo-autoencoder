from typing import List, Tuple

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_filtered = self.filter_non_x_characters(start)
        end_filtered = self.filter_non_x_characters(end)

        if len(start_filtered) != len(end_filtered):
            return False

        for (c1, i1), (c2, i2) in zip(start_filtered, end_filtered):
            if c1 != c2:
                return False
            if c1 == 'L' and i1 < i2:
                return False
            if c1 == 'R' and i1 > i2:
                return False

        return True

    def filter_non_x_characters(self, input_string: str) -> List[Tuple[str, int]]:
        return [(c, i) for i, c in enumerate(input_string) if c != 'X']