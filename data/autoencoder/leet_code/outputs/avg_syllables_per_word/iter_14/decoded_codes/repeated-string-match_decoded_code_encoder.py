class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        length_of_b = len(b)
        length_of_a = len(a)
        minimum_repeats = -(-length_of_b // length_of_a)  # Ceiling division

        if b in a * minimum_repeats:
            return minimum_repeats

        if b in a * (minimum_repeats + 1):
            return minimum_repeats + 1

        return -1