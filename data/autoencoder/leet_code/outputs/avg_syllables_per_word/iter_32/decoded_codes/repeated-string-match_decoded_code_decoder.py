import math

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Calculate the minimum repeats needed so that the length of repeated a >= length of b
        min_repeats = math.ceil(len(b) / len(a))

        # Check if b is substring of a repeated min_repeats times
        if b in a * min_repeats:
            return min_repeats

        # Check if b is substring of a repeated (min_repeats + 1) times
        if b in a * (min_repeats + 1):
            return min_repeats + 1

        return -1