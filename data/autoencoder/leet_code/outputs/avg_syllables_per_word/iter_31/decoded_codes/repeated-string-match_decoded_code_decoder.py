from math import ceil

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        minimum_repetitions = ceil(len(b) / len(a))
        repeated_a = a * minimum_repetitions
        if b in repeated_a:
            return minimum_repetitions
        repeated_a += a
        if b in repeated_a:
            return minimum_repetitions + 1
        return -1