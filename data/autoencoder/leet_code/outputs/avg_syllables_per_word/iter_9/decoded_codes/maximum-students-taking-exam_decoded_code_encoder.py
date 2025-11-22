class Solution:
    def maxStudents(self, seats):
        m, n = len(seats), len(seats[0])

        def broken_bitmask():
            broken = [0] * m
            for i in range(m):
                for j in range(n):
                    if seats[i][j] == '#':
                        broken[i] |= (1 << j)
            return broken

        def is_valid(arrangement):
            return (arrangement & (arrangement >> 1)) == 0

        broken = broken_bitmask()
        dp = [{} for _ in range(m)]

        for arrangement in range(1 << n):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(1 << n):
                if is_valid(arrangement) and (arrangement & broken[i]) == 0:
                    max_students = 0
                    for prev_arrangement in dp[i-1]:
                        if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                            max_students = max(max_students, dp[i-1][prev_arrangement])
                    if max_students or (max_students == 0 and dp[i-1]):
                        dp[i][arrangement] = max_students + bin(arrangement).count('1')

        return max(dp[-1].values()) if dp[-1] else 0