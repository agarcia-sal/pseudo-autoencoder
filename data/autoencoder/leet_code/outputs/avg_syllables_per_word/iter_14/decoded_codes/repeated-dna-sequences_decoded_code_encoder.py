from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sequence_count = defaultdict(int)
        length_of_s = len(s)
        limit = length_of_s - 9
        for index in range(limit):
            sequence = s[index:index + 10]
            sequence_count[sequence] += 1

        repeated_sequences = [seq for seq, count in sequence_count.items() if count > 1]
        return repeated_sequences