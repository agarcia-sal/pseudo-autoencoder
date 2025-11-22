class Solution:
    def maxStudents(self, seats):
        number_of_rows = len(seats)
        number_of_columns = len(seats[0]) if seats else 0

        broken = [0] * number_of_rows
        for i in range(number_of_rows):
            for j in range(number_of_columns):
                if seats[i][j] == '#':
                    broken[i] |= (1 << j)

        def is_valid(arrangement):
            # Valid if no two students sit adjacent horizontally
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(number_of_rows)]

        max_state = 1 << number_of_columns

        # Initialize dp for the first row
        for arrangement in range(max_state):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count("1")

        # Fill dp for subsequent rows
        for i in range(1, number_of_rows):
            for arrangement in range(max_state):
                if not is_valid(arrangement) or (arrangement & broken[i]) != 0:
                    continue

                max_students = 0
                for prev_arrangement, prev_count in dp[i - 1].items():
                    # Check no students are sitting diagonally adjacent from previous row
                    if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                        if prev_count > max_students:
                            max_students = prev_count

                dp[i][arrangement] = max_students + bin(arrangement).count("1")

        return max(dp[-1].values()) if dp and dp[-1] else 0