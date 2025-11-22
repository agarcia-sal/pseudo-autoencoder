from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sequence_count = defaultdict(int)
        for i in range(len(s) - 9):
            sequence_count[s[i:i+10]] += 1
        return [seq for seq, count in sequence_count.items() if count > 1]