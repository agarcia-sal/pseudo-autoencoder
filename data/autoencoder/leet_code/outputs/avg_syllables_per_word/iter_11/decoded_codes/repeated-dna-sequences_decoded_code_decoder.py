class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        sequence_count = {}
        for index in range(len(s) - 10 + 1):
            sequence = s[index:index+10]
            sequence_count[sequence] = sequence_count.get(sequence, 0) + 1
        repeated_sequences = []
        for sequence, count in sequence_count.items():
            if count > 1:
                repeated_sequences.append(sequence)
        return repeated_sequences