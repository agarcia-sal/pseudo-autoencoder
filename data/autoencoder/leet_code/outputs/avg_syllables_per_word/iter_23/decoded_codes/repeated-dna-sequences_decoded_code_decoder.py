from collections import defaultdict
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_count = defaultdict(int)
        for index in range(len(s) - 9):
            sequence = s[index:index+10]
            sequence_count[sequence] += 1
        repeated_sequences = [sequence for sequence, count in sequence_count.items() if count > 1]
        return repeated_sequences