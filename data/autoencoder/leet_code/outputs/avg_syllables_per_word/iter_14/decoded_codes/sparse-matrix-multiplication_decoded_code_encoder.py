class Solution:
    def multiply(self, mat1, mat2):
        number_of_rows_of_mat1 = len(mat1)
        number_of_columns_of_mat1 = len(mat1[0])
        number_of_rows_of_mat2 = len(mat2)
        number_of_columns_of_mat2 = len(mat2[0])

        def initialize_result_matrix(rows, columns):
            return [[0] * columns for _ in range(rows)]

        result = initialize_result_matrix(number_of_rows_of_mat1, number_of_columns_of_mat2)

        for row_index in range(number_of_rows_of_mat1):
            for column_index in range(number_of_columns_of_mat2):
                for middle_index in range(number_of_columns_of_mat1):
                    current_value = result[row_index][column_index]
                    multiplication_value = mat1[row_index][middle_index] * mat2[middle_index][column_index]
                    new_value = current_value + multiplication_value
                    result[row_index][column_index] = new_value

        return result