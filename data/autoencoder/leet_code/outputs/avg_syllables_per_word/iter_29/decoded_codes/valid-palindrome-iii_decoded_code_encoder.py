class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        def longest_palindromic_subseq(string_input: str) -> int:
            length_of_string = len(string_input)
            dp_matrix = [[0] * length_of_string for _ in range(length_of_string)]

            for index in range(length_of_string):
                dp_matrix[index][index] = 1

            for current_length in range(2, length_of_string + 1):
                for start_index in range(length_of_string - current_length + 1):
                    end_index = start_index + current_length - 1
                    if string_input[start_index] == string_input[end_index]:
                        dp_matrix[start_index][end_index] = dp_matrix[start_index + 1][end_index - 1] + 2
                    else:
                        dp_matrix[start_index][end_index] = max(dp_matrix[start_index + 1][end_index], dp_matrix[start_index][end_index - 1])

            return dp_matrix[0][length_of_string - 1]

        longest_palindrome_length = longest_palindromic_subseq(s)
        return (len(s) - longest_palindrome_length) <= k