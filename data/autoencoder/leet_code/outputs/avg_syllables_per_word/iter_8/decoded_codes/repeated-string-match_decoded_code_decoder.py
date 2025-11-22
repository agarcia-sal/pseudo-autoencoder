class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repeats = -(-len(b) // len(a))  # Ceiling division
        if b in a * min_repeats:
            return min_repeats
        elif b in a * (min_repeats + 1):
            return min_repeats + 1
        else:
            return -1