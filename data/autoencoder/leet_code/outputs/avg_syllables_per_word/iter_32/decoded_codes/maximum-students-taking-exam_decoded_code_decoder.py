from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0]) if seats else 0

        # Precompute the broken mask for each row: bit j is set if seat j is broken ('#')
        broken = [0] * m
        for i in range(m):
            row_mask = 0
            for j in range(n):
                if seats[i][j] == '#':
                    row_mask |= (1 << j)
            broken[i] = row_mask

        def is_valid(arrangement: int) -> bool:
            # arrangement invalid if any two adjacent bits are set (students sit next to each other in same row)
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(m)]

        max_arrangement = 1 << n

        # Initialize dp for row 0
        for arrangement in range(max_arrangement):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        # Fill dp for subsequent rows
        for i in range(1, m):
            for arrangement in range(max_arrangement):
                if not is_valid(arrangement):
                    continue
                if (arrangement & broken[i]) != 0:
                    continue

                max_students = 0
                for prev_arrangement in dp[i - 1]:
                    # No student in current row sits diagonally next to student in previous row
                    if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                        cur_students = dp[i - 1][prev_arrangement]
                        if cur_students > max_students:
                            max_students = cur_students

                if max_students or max_students == 0:
                    dp[i][arrangement] = max_students + bin(arrangement).count('1')

        if dp and dp[-1]:
            return max(dp[-1].values())
        else:
            return 0