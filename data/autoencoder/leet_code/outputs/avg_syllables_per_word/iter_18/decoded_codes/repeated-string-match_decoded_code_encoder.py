class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        minimum_repetitions = -(-len(b) // len(a))  # Ceiling division of len(b) by len(a)
        if b in a * minimum_repetitions:
            return minimum_repetitions
        if b in a * (minimum_repetitions + 1):
            return minimum_repetitions + 1
        return -1