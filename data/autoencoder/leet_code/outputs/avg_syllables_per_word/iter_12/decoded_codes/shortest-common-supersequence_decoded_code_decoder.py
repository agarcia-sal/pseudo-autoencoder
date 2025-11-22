class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
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

        # Build the shortest common supersequence by traversing dp table
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

        result = ''.join(scs)
        return result

    def create_dp_table(self, rows: int, columns: int) -> list:
        table = []
        for _ in range(rows):
            row = [0] * columns
            table.append(row)
        return table

    def reverse_list(self, list_to_reverse: list) -> None:
        start = 0
        end = len(list_to_reverse) - 1
        while start < end:
            list_to_reverse[start], list_to_reverse[end] = list_to_reverse[end], list_to_reverse[start]
            start += 1
            end -= 1