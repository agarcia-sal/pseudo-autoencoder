import math

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repetitions = -(-len(b) // len(a))  # Ceiling division

        if b in a * min_repetitions:
            return min_repetitions
        if b in a * (min_repetitions + 1):
            return min_repetitions + 1
        return -1