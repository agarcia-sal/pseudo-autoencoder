class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length_of_word1 = len(word1)
        length_of_word2 = len(word2)

        dp_table = [[0] * (length_of_word2 + 1) for _ in range(length_of_word1 + 1)]

        for index_i in range(length_of_word1 + 1):
            dp_table[index_i][0] = index_i

        for index_j in range(length_of_word2 + 1):
            dp_table[0][index_j] = index_j

        for index_i in range(1, length_of_word1 + 1):
            for index_j in range(1, length_of_word2 + 1):
                if word1[index_i - 1] == word2[index_j - 1]:
                    dp_table[index_i][index_j] = dp_table[index_i - 1][index_j - 1]
                else:
                    minimum_value = min(
                        dp_table[index_i - 1][index_j],      # deletion
                        dp_table[index_i][index_j - 1],      # insertion
                        dp_table[index_i - 1][index_j - 1]   # replacement
                    )
                    dp_table[index_i][index_j] = 1 + minimum_value

        return dp_table[length_of_word1][length_of_word2]