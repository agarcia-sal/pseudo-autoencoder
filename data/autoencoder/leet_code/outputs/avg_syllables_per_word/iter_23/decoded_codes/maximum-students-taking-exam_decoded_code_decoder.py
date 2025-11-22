class Solution:
    def maxStudents(self, seats):
        m = len(seats)
        n = len(seats[0]) if m > 0 else 0

        broken = [0] * m
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '#':
                    broken[i] |= (1 << j)

        def is_valid(arrangement):
            # arrangement must not have adjacent 1s
            # e.g., no two students sitting next to each other
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(m)]

        # Initialize dp for the first row
        for arrangement in range(1 << n):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(1 << n):
                if not is_valid(arrangement) or (arrangement & broken[i]) != 0:
                    continue
                max_students = 0
                for prev_arrangement, prev_count in dp[i - 1].items():
                    # students in arrangement cannot sit diagonally adjacent to students in prev_arrangement
                    if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                        if prev_count > max_students:
                            max_students = prev_count
                if max_students or i == 0 or len(dp[i - 1]) > 0:
                    dp[i][arrangement] = max_students + bin(arrangement).count('1')

        if dp[-1]:
            return max(dp[-1].values())
        return 0