class Solution:
    def isMatch(self, string_s: str, string_p: str) -> bool:
        m, n = len(string_s), len(string_p)
        dp_table = [[False] * (n + 1) for _ in range(m + 1)]
        dp_table[0][0] = True

        for j in range(1, n + 1):
            if string_p[j - 1] == '*':
                dp_table[0][j] = dp_table[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                s_char = string_s[i - 1]
                p_char = string_p[j - 1]

                if p_char == s_char or p_char == '.':
                    dp_table[i][j] = dp_table[i - 1][j - 1]
                elif p_char == '*':
                    dp_table[i][j] = dp_table[i][j - 2]
                    if string_p[j - 2] == s_char or string_p[j - 2] == '.':
                        dp_table[i][j] = dp_table[i][j] or dp_table[i - 1][j]

        return dp_table[m][n]