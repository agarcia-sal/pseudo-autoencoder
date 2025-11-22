class Solution:
    def minDistance(self, word1, word2):
        m = len(word1)
        n = len(word2)
        dp = self.create_2d_list(m + 1, n + 1, 0)
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    deletion_cost = dp[i - 1][j]
                    insertion_cost = dp[i][j - 1]
                    replacement_cost = dp[i - 1][j - 1]
                    dp[i][j] = 1 + min(deletion_cost, insertion_cost, replacement_cost)
        return dp[m][n]

    def create_2d_list(self, rows, columns, initial_value):
        new_list = []
        for _ in range(rows):
            new_row = []
            for _ in range(columns):
                new_row.append(initial_value)
            new_list.append(new_row)
        return new_list