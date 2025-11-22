class Solution:
    def maxStudents(self, seats):
        m = len(seats)
        n = len(seats[0])

        broken = [0] * m
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '#':
                    broken[i] |= (1 << j)

        def is_valid(arrangement):
            # No two students sitting adjacent in the same row
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(m)]

        max_mask = 1 << n
        for arrangement in range(max_mask):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(max_mask):
                if is_valid(arrangement) and (arrangement & broken[i]) == 0:
                    max_students = 0
                    for prev_arrangement, prev_count in dp[i - 1].items():
                        # No students seated diagonally adjacent between rows
                        if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                            if prev_count > max_students:
                                max_students = prev_count
                    if max_students or max_students == 0:
                        dp[i][arrangement] = max_students + bin(arrangement).count('1')

        return max(dp[-1].values()) if dp[-1] else 0