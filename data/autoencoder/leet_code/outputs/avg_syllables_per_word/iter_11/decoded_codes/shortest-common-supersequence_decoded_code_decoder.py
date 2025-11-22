class Solution:
    def shortestCommonSupersequence(self, str1, str2):
        m = len(str1)
        n = len(str2)
        dp = self.initialize_2D_list(m + 1, n + 1)

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
        return ''.join(scs)

    def initialize_2D_list(self, rows, columns):
        dp = []
        for _ in range(rows):
            row = []
            for _ in range(columns):
                row.append(0)
            dp.append(row)
        return dp

    def reverse_list(self, list_to_reverse):
        start = 0
        end = len(list_to_reverse) - 1
        while start < end:
            list_to_reverse[start], list_to_reverse[end] = list_to_reverse[end], list_to_reverse[start]
            start += 1
            end -= 1