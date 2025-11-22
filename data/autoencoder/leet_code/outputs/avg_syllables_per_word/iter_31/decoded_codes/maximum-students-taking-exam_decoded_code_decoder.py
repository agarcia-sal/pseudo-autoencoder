from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0]) if seats else 0

        broken = [0] * m
        for i in range(m):
            bitmask = 0
            for j in range(n):
                if seats[i][j] == '#':
                    bitmask |= 1 << j
            broken[i] = bitmask

        def is_valid(arrangement: int) -> bool:
            # No two students sitting adjacently in the same row
            return (arrangement & (arrangement >> 1)) == 0

        dp = [{} for _ in range(m)]

        max_mask = 1 << n
        for arrangement in range(max_mask):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(max_mask):
                if not (is_valid(arrangement) and (arrangement & broken[i]) == 0):
                    continue
                max_students = 0
                prev_dp = dp[i - 1]
                for prev_arrangement in prev_dp.keys():
                    # Check no student is sitting in front-left or front-right position
                    if (arrangement & (prev_arrangement >> 1)) == 0 and (arrangement & (prev_arrangement << 1)) == 0:
                        if prev_dp[prev_arrangement] > max_students:
                            max_students = prev_dp[prev_arrangement]
                dp[i][arrangement] = max_students + bin(arrangement).count('1')

        if dp and dp[-1]:
            return max(dp[-1].values())
        return 0