from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sequence_count = defaultdict(int)
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            sequence_count[sequence] += 1
        repeated_sequences = [sequence for sequence, count in sequence_count.items() if count > 1]
        return repeated_sequences