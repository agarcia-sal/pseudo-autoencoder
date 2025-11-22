from typing import List

class Solution:
    def maxStudents(self, seats: List[str]) -> int:
        m = len(seats)
        n = len(seats[0]) if m > 0 else 0

        broken = [0] * m
        for i in range(m):
            for j in range(n):
                if seats[i][j] == '#':
                    broken[i] |= (1 << j)

        def is_valid(arrangement: int) -> bool:
            # No two students sitting next to each other in the same row
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(m)]

        limit = 1 << n
        for arrangement in range(limit):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(limit):
                if is_valid(arrangement) and (arrangement & broken[i]) == 0:
                    max_students = 0
                    prev_dp = dp[i - 1]
                    for prev_arrangement in prev_dp:
                        # Students cannot sit diagonally adjacent in consecutive rows
                        if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                            if prev_dp[prev_arrangement] > max_students:
                                max_students = prev_dp[prev_arrangement]
                    if max_students or (max_students == 0 and dp[i-1]):
                        dp[i][arrangement] = max_students + bin(arrangement).count('1')

        return max(dp[m - 1].values()) if dp[m - 1] else 0