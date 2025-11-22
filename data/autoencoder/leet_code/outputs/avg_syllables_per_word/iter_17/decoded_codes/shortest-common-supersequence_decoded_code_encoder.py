class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp_table = self.construct_dp_table(m, n)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp_table[i][j] = dp_table[i - 1][j - 1] + 1
                else:
                    dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])

        i, j = m, n
        scs = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                scs.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp_table[i - 1][j] > dp_table[i][j - 1]:
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
        return self.join_characters(scs)

    def construct_dp_table(self, m: int, n: int) -> list[list[int]]:
        return [[0] * (n + 1) for _ in range(m + 1)]

    def reverse_list(self, list_to_reverse: list) -> None:
        list_to_reverse.reverse()

    def join_characters(self, list_of_characters: list[str]) -> str:
        return ''.join(list_of_characters)