from collections import Counter
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        sequence_count = Counter()
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            sequence_count[sequence] += 1
        return [seq for seq, count in sequence_count.items() if count > 1]