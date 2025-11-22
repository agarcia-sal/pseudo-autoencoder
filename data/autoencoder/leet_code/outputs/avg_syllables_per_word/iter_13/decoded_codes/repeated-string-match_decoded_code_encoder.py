import math

class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Calculate the minimum number of repetitions needed (ceiling division)
        min_reps = math.ceil(len(b) / len(a))

        if b in a * min_reps:
            return min_reps
        if b in a * (min_reps + 1):
            return min_reps + 1
        return -1