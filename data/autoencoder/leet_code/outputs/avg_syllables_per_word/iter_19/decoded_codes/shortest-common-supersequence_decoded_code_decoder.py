class Solution:
    def shortestCommonSupersequence(self, str1, str2):
        m = len(str1)
        n = len(str2)

        dp = self.create_dp_table(m + 1, n + 1)

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

        scs_reversed = self.reverse_list(scs)
        result_string = self.join_characters_in_list(scs_reversed)
        return result_string

    def create_dp_table(self, rows, columns):
        return [[0] * columns for _ in range(rows)]

    def reverse_list(self, input_list):
        return input_list[::-1]

    def join_characters_in_list(self, character_list):
        return ''.join(character_list)