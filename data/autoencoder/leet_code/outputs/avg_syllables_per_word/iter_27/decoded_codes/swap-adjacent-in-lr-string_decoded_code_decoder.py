from typing import List, Tuple

class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_filtered: List[Tuple[str, int]] = [(ch, i) for i, ch in enumerate(start) if ch != 'X']
        end_filtered: List[Tuple[str, int]] = [(ch, i) for i, ch in enumerate(end) if ch != 'X']

        if len(start_filtered) != len(end_filtered):
            return False

        for (ch1, i1), (ch2, i2) in zip(start_filtered, end_filtered):
            if ch1 != ch2:
                return False
            if ch1 == 'L' and i1 < i2:
                return False
            if ch1 == 'R' and i1 > i2:
                return False

        return True