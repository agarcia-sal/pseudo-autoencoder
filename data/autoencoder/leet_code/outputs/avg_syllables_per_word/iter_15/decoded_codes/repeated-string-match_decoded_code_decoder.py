class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        # Calculate the minimum number of repeats to cover length of b
        minimum_repeats = -(-len(b) // len(a))  # Ceiling division
        if b in a * minimum_repeats:
            return minimum_repeats
        if b in a * (minimum_repeats + 1):
            return minimum_repeats + 1
        return -1