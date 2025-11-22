import math

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repetitions = math.ceil(len(b) / len(a))
        repeated_a = a * min_repetitions
        if b in repeated_a:
            return min_repetitions
        if b in (repeated_a + a):
            return min_repetitions + 1
        return -1