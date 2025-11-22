import math

class Solution:
    def repeatedStringMatch(self, a_string: str, b_string: str) -> int:
        minimum_repetitions = math.ceil(len(b_string) / len(a_string))
        if b_string in a_string * minimum_repetitions:
            return minimum_repetitions
        if b_string in a_string * (minimum_repetitions + 1):
            return minimum_repetitions + 1
        return -1