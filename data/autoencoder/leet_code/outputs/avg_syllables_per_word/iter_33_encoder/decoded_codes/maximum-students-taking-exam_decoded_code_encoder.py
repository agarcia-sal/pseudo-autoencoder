class Solution:
    def maxStudents(self, seats):
        m = len(seats)
        n = len(seats[0]) if m > 0 else 0

        broken = [0] * m
        for i in range(m):
            row_mask = 0
            for j in range(n):
                if seats[i][j] == '#':
                    row_mask |= 1 << j
            broken[i] = row_mask

        def is_valid(arrangement):
            # Must not have two adjacent students in the same row
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(m)]

        limit = 1 << n

        # Initialize dp for the first row
        for arrangement in range(limit):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(limit):
                if not is_valid(arrangement) or (arrangement & broken[i]) != 0:
                    continue
                max_students = 0
                for prev_arrangement, prev_count in dp[i - 1].items():
                    # No student sits to the immediate left or right from previous row to current
                    if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                        if prev_count > max_students:
                            max_students = prev_count
                if max_students or dp[i - 1]:
                    dp[i][arrangement] = max_students + bin(arrangement).count('1')

        if dp[m - 1]:
            return max(dp[m - 1].values())
        return 0