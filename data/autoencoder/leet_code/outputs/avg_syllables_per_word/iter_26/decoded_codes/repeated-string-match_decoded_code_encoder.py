class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        minimum_repetitions = -(-len(b) // len(a))  # ceiling division of len(b) / len(a)
        if b in a * minimum_repetitions:
            return minimum_repetitions
        if b in a * (minimum_repetitions + 1):
            return minimum_repetitions + 1
        return -1