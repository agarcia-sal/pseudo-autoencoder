class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        dp = self.create_2D_list(m + 1, n + 1, 0)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j = m, n
        scs = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                scs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                scs.append(str1[i - 1])
                i -= 1
            else:
                scs.append(str2[j - 1])
                j -= 1

        while i > 0:
            scs.append(str1[i - 1])
            i -= 1

        while j > 0:
            scs.append(str2[j - 1])
            j -= 1

        self.reverse_list(scs)
        result_string = self.join_characters_of_list(scs)
        return result_string

    def create_2D_list(self, rows: int, columns: int, initial_value):
        two_dimensional_list = []
        for _ in range(rows):
            row_list = []
            for _ in range(columns):
                row_list.append(initial_value)
            two_dimensional_list.append(row_list)
        return two_dimensional_list

    def reverse_list(self, list_to_reverse):
        left_index = 0
        right_index = len(list_to_reverse) - 1
        while left_index < right_index:
            list_to_reverse[left_index], list_to_reverse[right_index] = list_to_reverse[right_index], list_to_reverse[left_index]
            left_index += 1
            right_index -= 1

    def join_characters_of_list(self, character_list):
        combined_string = ""
        for character in character_list:
            combined_string += character
        return combined_string