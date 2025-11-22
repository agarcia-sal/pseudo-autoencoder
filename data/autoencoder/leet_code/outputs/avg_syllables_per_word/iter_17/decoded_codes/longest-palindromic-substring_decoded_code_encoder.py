class Solution:
    def longestPalindrome(self, string_s: str) -> str:
        length_n = len(string_s)
        # Initialize the DP matrix with True on the diagonal and False elsewhere
        matrix_f = [[True] * length_n for _ in range(length_n)]
        variable_k = 0
        variable_mx = 1

        for index_i in range(length_n - 2, -1, -1):
            for index_j in range(index_i + 1, length_n):
                matrix_f[index_i][index_j] = False
                if string_s[index_i] == string_s[index_j]:
                    if index_j - index_i == 1:
                        matrix_f[index_i][index_j] = True
                    else:
                        matrix_f[index_i][index_j] = matrix_f[index_i + 1][index_j - 1]
                    if matrix_f[index_i][index_j] and variable_mx < index_j - index_i + 1:
                        variable_k = index_i
                        variable_mx = index_j - index_i + 1

        return string_s[variable_k:variable_k + variable_mx]