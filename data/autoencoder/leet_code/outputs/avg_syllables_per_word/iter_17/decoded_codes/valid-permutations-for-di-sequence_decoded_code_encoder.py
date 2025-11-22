class Solution:
    def numPermsDISequence(self, sequence_string: str) -> int:
        MODULO_VALUE = 10**9 + 7
        sequence_length = len(sequence_string)

        # Initialize a 2D list (dp_table) of dimensions (sequence_length + 1) x (sequence_length + 1) with zeros
        dp_table = [[0] * (sequence_length + 1) for _ in range(sequence_length + 1)]

        # Base case: For i=0, dp_table[0][j] = 1 for all j
        for j in range(sequence_length + 1):
            dp_table[0][j] = 1

        for i in range(1, sequence_length + 1):
            running_prefix_sum = 0
            if sequence_string[i - 1] == 'I':
                for j in range(sequence_length + 1 - i):
                    running_prefix_sum = (running_prefix_sum + dp_table[i - 1][j]) % MODULO_VALUE
                    dp_table[i][j] = running_prefix_sum
            else:  # 'D'
                for j in range(sequence_length - i, -1, -1):
                    running_prefix_sum = (running_prefix_sum + dp_table[i - 1][j + 1]) % MODULO_VALUE
                    dp_table[i][j] = running_prefix_sum

        total_permutations = sum(dp_table[sequence_length]) % MODULO_VALUE
        return total_permutations