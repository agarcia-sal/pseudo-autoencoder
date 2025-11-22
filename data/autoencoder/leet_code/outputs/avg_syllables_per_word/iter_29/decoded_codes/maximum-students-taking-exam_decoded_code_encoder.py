class Solution:
    def maxStudents(self, seats):
        number_of_rows = len(seats)
        number_of_columns = len(seats[0]) if number_of_rows > 0 else 0

        broken_seats = [0] * number_of_rows
        for index_row in range(number_of_rows):
            for index_column in range(number_of_columns):
                if seats[index_row][index_column] == '#':
                    broken_seats[index_row] |= (1 << index_column)

        def is_valid(arrangement):
            # No two students sitting next to each other in the same row
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(number_of_rows)]

        for arrangement in range(1 << number_of_columns):
            if is_valid(arrangement) and (arrangement & broken_seats[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for index_row in range(1, number_of_rows):
            for arrangement in range(1 << number_of_columns):
                if not is_valid(arrangement) or (arrangement & broken_seats[index_row]) != 0:
                    continue
                max_students = 0
                for prev_arrangement in dp[index_row - 1]:
                    # Check no students sitting diagonally adjacent between rows
                    if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                        if dp[index_row - 1][prev_arrangement] > max_students:
                            max_students = dp[index_row - 1][prev_arrangement]
                dp[index_row][arrangement] = max_students + bin(arrangement).count('1')

        return max(dp[-1].values()) if dp and dp[-1] else 0