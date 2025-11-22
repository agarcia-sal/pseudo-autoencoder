class Solution:
    def findRepeatedDnaSequences(self, s):
        sequence_count = {}
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            sequence_count[sequence] = sequence_count.get(sequence, 0) + 1
        repeated_sequences = []
        for sequence, count in sequence_count.items():
            if count > 1:
                repeated_sequences.append(sequence)
        return repeated_sequences