from collections import defaultdict
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, string_s: str) -> List[str]:
        sequence_count = defaultdict(int)
        for index in range(len(string_s) - 9):
            sequence = string_s[index:index + 10]
            sequence_count[sequence] += 1
        repeated_sequences = [seq for seq, count in sequence_count.items() if count > 1]
        return repeated_sequences