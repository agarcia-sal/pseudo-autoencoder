class Solution:
    def minTotalDistance(self, grid):
        list_of_row_indices = []
        list_of_column_indices = []

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    list_of_row_indices.append(i)
                    list_of_column_indices.append(j)

        list_of_row_indices.sort()
        list_of_column_indices.sort()

        middle_index_for_rows = len(list_of_row_indices) // 2
        middle_index_for_columns = len(list_of_column_indices) // 2

        median_row = list_of_row_indices[middle_index_for_rows]
        median_column = list_of_column_indices[middle_index_for_columns]

        minimum_total_distance = 0
        for row_index in list_of_row_indices:
            minimum_total_distance += abs(row_index - median_row)
        for column_index in list_of_column_indices:
            minimum_total_distance += abs(column_index - median_column)

        return minimum_total_distance