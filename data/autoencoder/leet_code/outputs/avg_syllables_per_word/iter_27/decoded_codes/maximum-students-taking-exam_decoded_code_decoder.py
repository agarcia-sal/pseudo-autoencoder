from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        if m == 0:
            return 0
        n = len(seats[0])
        if n == 0:
            return 0

        broken = [0] * m
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '#':
                    broken[i] |= (1 << j)

        def is_valid(arrangement: int) -> bool:
            # check no two adjacent seats are taken in the same row
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(m)]

        # Initialize dp for the first row
        for arrangement in range(1 << n):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        # Fill dp for subsequent rows
        for i in range(1, m):
            for arrangement in range(1 << n):
                if is_valid(arrangement) and (arrangement & broken[i]) == 0:
                    max_students = 0
                    for prev_arrangement, prev_count in dp[i - 1].items():
                        # No cheating by sitting diagonally adjacent between rows
                        if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                            if prev_count > max_students:
                                max_students = prev_count
                    dp[i][arrangement] = max_students + bin(arrangement).count('1')

        if dp[-1]:
            return max(dp[-1].values())
        return 0