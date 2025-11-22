from typing import List


class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0]) if m > 0 else 0

        broken = [0] * m
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '#':
                    broken[i] |= 1 << j

        def is_valid(arrangement: int) -> bool:
            # No two students sitting next to each other in the same row
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(m)]

        for arrangement in range(1 << n):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(1 << n):
                if not is_valid(arrangement) or (arrangement & broken[i]) != 0:
                    continue
                max_students = 0
                for prev_arrangement in dp[i - 1]:
                    # No student in current arrangement should be left-top or right-top diagonal to any student in the previous row
                    if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                        max_students = max(max_students, dp[i - 1][prev_arrangement])
                if max_students or i == 1:  # Optimize: avoid empty dp except for i=1 rows
                    dp[i][arrangement] = max_students + bin(arrangement).count('1')

        return max(dp[m - 1].values()) if dp[m - 1] else 0