from typing import List, Tuple

class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MODULUS = 10 ** 9 + 1

        def generate_valid_columns(prev_col: Tuple[int, ...] | None) -> List[Tuple[int, ...]]:
            colors_list = [1, 2, 3]
            valid_columns_list: List[Tuple[int, ...]] = []

            def backtrack(current_column: List[int], current_row: int) -> None:
                if current_row == m:
                    valid_columns_list.append(tuple(current_column))
                    return
                for color in colors_list:
                    if len(current_column) == 0 or current_column[-1] != color:
                        if prev_col is not None and prev_col[current_row] == color:
                            continue
                        current_column.append(color)
                        backtrack(current_column, current_row + 1)
                        current_column.pop()

            backtrack([], 0)
            return valid_columns_list

        all_valid_columns = generate_valid_columns(None)
        number_of_valid_columns = len(all_valid_columns)

        compatible_columns_mapping: dict[int, List[int]] = {i: [] for i in range(number_of_valid_columns)}
        for index_i in range(number_of_valid_columns):
            col_i = all_valid_columns[index_i]
            for index_j in range(number_of_valid_columns):
                col_j = all_valid_columns[index_j]
                all_positions_different = True
                for position_k in range(m):
                    if col_i[position_k] == col_j[position_k]:
                        all_positions_different = False
                        break
                if all_positions_different:
                    compatible_columns_mapping[index_i].append(index_j)

        dp_table = [1] * number_of_valid_columns

        for _ in range(1, n):
            next_dp_table = [0] * number_of_valid_columns
            for index_i in range(number_of_valid_columns):
                count = dp_table[index_i]
                if count == 0:
                    continue
                for index_j in compatible_columns_mapping[index_i]:
                    next_dp_table[index_j] = (next_dp_table[index_j] + count) % MODULUS
            dp_table = next_dp_table

        total_ways = sum(dp_table) % MODULUS

        return total_ways