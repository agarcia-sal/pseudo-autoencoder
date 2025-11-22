class Solution:
    def longestPalindrome(self, s: str) -> str:
        string_length = len(s)
        # Initialize palindrome_table with True for all substrings of length 1 and empty entries for others
        palindrome_table = [[False] * string_length for _ in range(string_length)]

        # All substrings of length 1 are palindromes
        for i in range(string_length):
            palindrome_table[i][i] = True

        start_index = 0
        maximum_length = 1

        for index_i in range(string_length - 2, -1, -1):
            for index_j in range(index_i + 1, string_length):
                palindrome_table[index_i][index_j] = False
                if s[index_i] == s[index_j]:
                    if index_j - index_i == 1:
                        palindrome_table[index_i][index_j] = True
                    else:
                        palindrome_table[index_i][index_j] = palindrome_table[index_i + 1][index_j - 1]
                if palindrome_table[index_i][index_j] and maximum_length < (index_j - index_i + 1):
                    start_index = index_i
                    maximum_length = index_j - index_i + 1

        return s[start_index:start_index + maximum_length]