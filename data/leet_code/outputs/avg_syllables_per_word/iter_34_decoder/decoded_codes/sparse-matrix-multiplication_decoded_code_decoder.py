class Solution:
    def multiply(self, mat1, mat2):
        number_of_rows_in_mat1 = len(mat1)
        number_of_columns_in_mat1 = len(mat1[0])
        number_of_rows_in_mat2 = len(mat2)
        number_of_columns_in_mat2 = len(mat2[0])

        result = [[0] * number_of_columns_in_mat2 for _ in range(number_of_rows_in_mat1)]

        for index_i in range(number_of_rows_in_mat1):
            for index_j in range(number_of_columns_in_mat2):
                for index_p in range(number_of_columns_in_mat1):
                    result[index_i][index_j] += mat1[index_i][index_p] * mat2[index_p][index_j]

        return result