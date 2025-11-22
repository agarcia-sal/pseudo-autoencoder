from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s):
        sequence_count = defaultdict(int)
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            sequence_count[sequence] += 1
        repeated_sequences = []
        for seq, count in sequence_count.items():
            if count > 1:
                repeated_sequences.append(seq)
        return repeated_sequences