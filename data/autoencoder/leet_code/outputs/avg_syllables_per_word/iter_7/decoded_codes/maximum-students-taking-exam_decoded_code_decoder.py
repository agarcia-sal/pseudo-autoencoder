from typing import List, Dict

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0]) if m > 0 else 0

        broken = [0] * m
        for i in range(m):
            row_bits = 0
            for j in range(n):
                if seats[i][j] == '#':
                    row_bits |= 1 << j
            broken[i] = row_bits

        def is_valid(arrangement: int) -> bool:
            # No two students sitting next to each other in the same row
            return (arrangement & (arrangement >> 1)) == 0

        dp: List[Dict[int, int]] = [{} for _ in range(m)]

        for arrangement in range(1 << n):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(1 << n):
                if not is_valid(arrangement) or (arrangement & broken[i]) != 0:
                    continue
                max_students = 0
                for prev_arrangement in dp[i - 1]:
                    if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                        if dp[i - 1][prev_arrangement] > max_students:
                            max_students = dp[i - 1][prev_arrangement]
                if max_students + bin(arrangement).count('1') > 0:
                    dp[i][arrangement] = max_students + bin(arrangement).count('1')

        return max(dp[m - 1].values()) if dp[m - 1] else 0