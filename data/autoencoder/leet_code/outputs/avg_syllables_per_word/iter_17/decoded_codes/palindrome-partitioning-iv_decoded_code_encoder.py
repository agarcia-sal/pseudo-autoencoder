class Solution:
    def checkPartitioning(self, string_input: str) -> bool:
        def is_palindrome(substring_input: str) -> bool:
            return substring_input == substring_input[::-1]

        length_n = len(string_input)

        palindrome_status_matrix = self.initialize_palindrome_status(length_n)

        for index_i in range(length_n - 1, -1, -1):
            for index_j in range(index_i, length_n):
                if (string_input[index_i] == string_input[index_j] and 
                    (index_j - index_i <= 1 or palindrome_status_matrix[index_i + 1][index_j - 1])):
                    palindrome_status_matrix[index_i][index_j] = True

        for first_partition_index in range(1, length_n - 1):
            if palindrome_status_matrix[0][first_partition_index - 1]:
                for second_partition_index in range(first_partition_index, length_n - 1):
                    if (palindrome_status_matrix[first_partition_index][second_partition_index] and 
                        palindrome_status_matrix[second_partition_index + 1][length_n - 1]):
                        return True

        return False

    def initialize_palindrome_status(self, length_n: int):
        return [[False] * length_n for _ in range(length_n)]