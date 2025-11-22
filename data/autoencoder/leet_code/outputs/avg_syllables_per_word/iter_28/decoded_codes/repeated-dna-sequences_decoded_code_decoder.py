from collections import Counter
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_count = Counter(s[i:i+10] for i in range(len(s) - 9))
        return [seq for seq, count in sequence_count.items() if count > 1]