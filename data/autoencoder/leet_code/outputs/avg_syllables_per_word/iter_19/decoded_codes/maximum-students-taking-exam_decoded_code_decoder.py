class Solution:
    def maxStudents(self, seats):
        m = len(seats)
        n = len(seats[0]) if m > 0 else 0

        broken = [0] * m
        for i in range(m):
            row_mask = 0
            for j in range(n):
                if seats[i][j] == '#':  # '#' represents a broken seat
                    row_mask |= 1 << j
            broken[i] = row_mask

        def is_valid(arrangement):
            # no two students adjacent in a row: arrangement & (arrangement >> 1) == 0
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(m)]

        max_state = 1 << n
        for arrangement in range(max_state):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(max_state):
                if is_valid(arrangement) and (arrangement & broken[i]) == 0:
                    max_students = 0
                    for prev_arrangement in dp[i - 1]:
                        if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                            max_students = max(max_students, dp[i - 1][prev_arrangement])
                    dp[i][arrangement] = max_students + bin(arrangement).count('1')

        return max(dp[m - 1].values()) if dp[m - 1] else 0