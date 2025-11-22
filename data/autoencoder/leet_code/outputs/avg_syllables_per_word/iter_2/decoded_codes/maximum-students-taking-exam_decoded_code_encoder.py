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
            return (arrangement & (arrangement >> 1)) == 0

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
                    dp[i][arrangement] = max_students + bin(arrangement).count('1')

        if dp[m-1]:
            return max(dp[m-1].values())
        else:
            return 0