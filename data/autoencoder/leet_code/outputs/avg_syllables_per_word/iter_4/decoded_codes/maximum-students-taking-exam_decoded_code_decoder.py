from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0]) if m > 0 else 0

        broken = [0] * m
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '#':
                    broken[i] |= (1 << j)

        def is_valid(arrangement: int) -> bool:
            # Check that no two students sit adjacently in the same row
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(m)]

        max_state = 1 << n

        # Initialize dp for the first row
        for arrangement in range(max_state):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(max_state):
                if not is_valid(arrangement):
                    continue
                if (arrangement & broken[i]) != 0:
                    continue

                max_students = 0
                for prev_arrangement in dp[i-1]:
                    # No cheating conditions:
                    # No student directly to the left-up or right-up diagonal
                    if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                        max_students = max(max_students, dp[i-1][prev_arrangement])

                if max_students > 0 or i == 0 or len(dp[i-1]) > 0:
                    dp[i][arrangement] = max_students + bin(arrangement).count('1')

        if dp[m-1]:
            return max(dp[m-1].values())
        return 0