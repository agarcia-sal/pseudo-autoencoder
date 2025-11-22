class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MODULO = 10**9 + 7

        def generate_valid_columns(previous_column):
            color_options = [1, 2, 3]
            list_of_valid_columns = []

            def backtrack(current_column, current_row):
                if current_row == m:
                    list_of_valid_columns.append(tuple(current_column))
                    return
                for color in color_options:
                    if not current_column or current_column[-1] != color:
                        if previous_column is not None and previous_column[current_row] == color:
                            continue
                        current_column.append(color)
                        backtrack(current_column, current_row + 1)
                        current_column.pop()

            backtrack([], 0)
            return list_of_valid_columns

        list_of_all_valid_columns = generate_valid_columns(None)
        number_of_valid_columns = len(list_of_all_valid_columns)

        dictionary_of_compatible_columns = {i: [] for i in range(number_of_valid_columns)}
        for i in range(number_of_valid_columns):
            col_i = list_of_all_valid_columns[i]
            for j in range(number_of_valid_columns):
                col_j = list_of_all_valid_columns[j]
                condition_hold = True
                for k in range(m):
                    if col_i[k] == col_j[k]:
                        condition_hold = False
                        break
                if condition_hold:
                    dictionary_of_compatible_columns[i].append(j)

        dynamic_programming_list = [1] * number_of_valid_columns

        for _ in range(n - 1):
            next_dynamic_programming_list = [0] * number_of_valid_columns
            for i in range(number_of_valid_columns):
                count = dynamic_programming_list[i]
                if count == 0:
                    continue
                for compatible_index in dictionary_of_compatible_columns[i]:
                    next_dynamic_programming_list[compatible_index] = (next_dynamic_programming_list[compatible_index] + count) % MODULO
            dynamic_programming_list = next_dynamic_programming_list

        total_ways = sum(dynamic_programming_list) % MODULO

        return total_ways