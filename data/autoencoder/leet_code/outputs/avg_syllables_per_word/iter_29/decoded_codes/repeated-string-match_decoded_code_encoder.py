import math

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        minimum_repeats = math.ceil(len(b) / len(a))
        if b in a * minimum_repeats:
            return minimum_repeats
        if b in a * (minimum_repeats + 1):
            return minimum_repeats + 1
        return -1