class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_filtered = []
        end_filtered = []

        for i in range(len(start)):
            c = start[i]
            if c != 'X':
                start_filtered.append((c, i))

        for i in range(len(end)):
            c = end[i]
            if c != 'X':
                end_filtered.append((c, i))

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