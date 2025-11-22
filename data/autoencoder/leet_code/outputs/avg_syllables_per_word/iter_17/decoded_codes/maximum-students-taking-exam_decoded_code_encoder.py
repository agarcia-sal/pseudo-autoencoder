from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0]) if m > 0 else 0

        def convertSeatsToBitmask(seats: List[List[str]]) -> List[int]:
            number_of_rows = len(seats)
            number_of_columns = len(seats[0]) if number_of_rows > 0 else 0
            broken_mask_list = [0] * number_of_rows
            for row_index in range(number_of_rows):
                current_mask = 0
                for column_index in range(number_of_columns):
                    if seats[row_index][column_index] == '#':
                        current_mask |= 1 << column_index
                broken_mask_list[row_index] = current_mask
            return broken_mask_list

        def is_valid(arrangement: int) -> bool:
            # No two students sitting next to each other horizontally
            return (arrangement & (arrangement >> 1)) == 0

        broken = convertSeatsToBitmask(seats)
        dp = [{} for _ in range(m)]

        # Initialize dp for first row
        for arrangement in range(1 << n):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for row_index in range(1, m):
            for arrangement in range(1 << n):
                if is_valid(arrangement) and (arrangement & broken[row_index]) == 0:
                    max_students = 0
                    for prev_arrangement in dp[row_index - 1]:
                        # Check no student sits next to each other in adjacent rows diagonally
                        if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                            max_students = max(max_students, dp[row_index - 1][prev_arrangement])
                    dp[row_index][arrangement] = max_students + bin(arrangement).count('1')

        if dp[m - 1]:
            return max(dp[m - 1].values())
        else:
            return 0