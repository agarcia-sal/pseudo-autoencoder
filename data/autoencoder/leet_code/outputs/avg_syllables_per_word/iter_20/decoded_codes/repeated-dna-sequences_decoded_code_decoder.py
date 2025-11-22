from collections import defaultdict
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        counts = defaultdict(int)
        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            counts[sequence] += 1
        repeated_sequences = [seq for seq, cnt in counts.items() if cnt > 1]
        return repeated_sequences