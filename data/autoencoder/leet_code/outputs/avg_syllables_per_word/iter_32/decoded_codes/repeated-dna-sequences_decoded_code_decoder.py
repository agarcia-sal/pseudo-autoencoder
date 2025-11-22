from collections import defaultdict
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_count = defaultdict(int)
        length = len(s)
        # Iterate through s to get all 10-letter-long sequences
        for i in range(length - 10 + 1):
            sequence = s[i:i+10]
            sequence_count[sequence] += 1

        # Collect sequences that appear more than once
        repeated_sequences = [seq for seq, count in sequence_count.items() if count > 1]
        return repeated_sequences