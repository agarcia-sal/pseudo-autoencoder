from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s):
        sequence_count = defaultdict(int)
        for index in range(len(s) - 9):
            sequence = s[index:index+10]
            sequence_count[sequence] += 1
        repeated_sequences = [seq for seq, count in sequence_count.items() if count > 1]
        return repeated_sequences