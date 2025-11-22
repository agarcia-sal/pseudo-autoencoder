class Solution:
    def maxStudents(self, seats):
        m, n = len(seats), len(seats[0])
        broken = [0] * m
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '#':
                    broken[i] |= 1 << j

        def is_valid(arrangement):
            return (arrangement & (arrangement >> 1)) == 0

        dp = [dict() for _ in range(m)]

        for arrangement in range(1 << n):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(1 << n):
                if not is_valid(arrangement) or (arrangement & broken[i]) != 0:
                    continue
                max_students = 0
                prev_dp = dp[i - 1]
                for prev_arrangement in prev_dp:
                    if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                        max_students = max(max_students, prev_dp[prev_arrangement])
                if max_students or max_students == 0 and prev_dp:
                    dp[i][arrangement] = max_students + bin(arrangement).count('1')

        return max(dp[-1].values()) if dp[-1] else 0