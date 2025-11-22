class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        from math import ceil
        min_repeats = ceil(len(b) / len(a))
        if b in a * min_repeats:
            return min_repeats
        elif b in a * (min_repeats + 1):
            return min_repeats + 1
        else:
            return -1