from math import inf

class Solution:
    def calculateMinimumHP(self, dungeon):
        number_of_rows = len(dungeon)
        number_of_columns = len(dungeon[0])

        dp = [[inf] * (number_of_columns + 1) for _ in range(number_of_rows + 1)]
        dp[number_of_rows][number_of_columns - 1] = 1
        dp[number_of_rows - 1][number_of_columns] = 1

        for row_index in range(number_of_rows - 1, -1, -1):
            for column_index in range(number_of_columns - 1, -1, -1):
                minimum_health_needed = min(dp[row_index + 1][column_index], dp[row_index][column_index + 1]) - dungeon[row_index][column_index]
                dp[row_index][column_index] = max(minimum_health_needed, 1)

        return dp[0][0]