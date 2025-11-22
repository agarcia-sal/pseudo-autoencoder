class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_filtered = [(c, i) for i, c in enumerate(start) if c != 'X']
        end_filtered = [(c, i) for i, c in enumerate(end) if c != 'X']

        if len(start_filtered) != len(end_filtered):
            return False

        for (char1, index1), (char2, index2) in zip(start_filtered, end_filtered):
            if char1 != char2:
                return False
            if char1 == 'L' and index1 < index2:
                return False
            if char1 == 'R' and index1 > index2:
                return False

        return True