class Solution:
    def maxStudents(self, seats):
        m = len(seats)
        n = len(seats[0]) if m > 0 else 0

        broken = [0] * m
        for i in range(m):
            row_mask = 0
            for j in range(n):
                if seats[i][j] == '#':
                    row_mask |= (1 << j)
            broken[i] = row_mask

        def is_valid(arrangement):
            # Check no two adjacent students in the same row
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(m)]

        limit = 1 << n
        # Initialize dp for the first row
        for arrangement in range(limit):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(limit):
                if is_valid(arrangement) and (arrangement & broken[i]) == 0:
                    max_students = 0
                    for prev_arrangement in dp[i - 1]:
                        # Check no student can cheat sideways with the previous row
                        if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                            if dp[i - 1][prev_arrangement] > max_students:
                                max_students = dp[i - 1][prev_arrangement]
                    if max_students or arr_match := (dp[i - 1]):
                        # Only store if there's a valid previous row arrangement or the first valid arrangement in this row
                        dp[i][arrangement] = max_students + bin(arrangement).count('1')

        return max(dp[m - 1].values()) if dp[m - 1] else 0