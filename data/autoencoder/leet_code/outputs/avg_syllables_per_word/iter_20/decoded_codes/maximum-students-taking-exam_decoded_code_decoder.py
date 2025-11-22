from typing import List

class Solution:
    def maxStudents(self, seats: List[List[str]]) -> int:
        m = len(seats)
        n = len(seats[0]) if m > 0 else 0

        def convertSeatsToBroken(seats: List[List[str]]) -> List[int]:
            broken = [0] * m
            for i in range(m):
                row_bits = 0
                for j in range(n):
                    if seats[i][j] == '#':
                        row_bits |= 1 << j
                broken[i] = row_bits
            return broken

        def is_valid(arrangement: int) -> bool:
            # no two students sitting side by side in the arrangement
            return (arrangement & (arrangement >> 1)) == 0

        if m == 0 or n == 0:
            return 0

        broken = convertSeatsToBroken(seats)

        # dp[i]: dict mapping arrangement (bitmask) to max students seated up to row i
        dp = [{} for _ in range(m)]

        max_mask = (1 << n) - 1

        # Initialize dp[0]
        for arrangement in range(max_mask + 1):
            if is_valid(arrangement) and (arrangement & broken[0]) == 0:
                dp[0][arrangement] = bin(arrangement).count('1')

        for i in range(1, m):
            for arrangement in range(max_mask + 1):
                if not is_valid(arrangement) or (arrangement & broken[i]) != 0:
                    continue

                max_students = 0
                dp_prev = dp[i - 1]
                if not dp_prev:
                    continue

                for prev_arrangement in dp_prev.keys():
                    # no "kissing" (diagonal) students: arrangement & (prev_arrangement << 1) == 0 and arrangement & (prev_arrangement >> 1) == 0
                    if (arrangement & (prev_arrangement << 1)) == 0 and (arrangement & (prev_arrangement >> 1)) == 0:
                        if dp_prev[prev_arrangement] > max_students:
                            max_students = dp_prev[prev_arrangement]
                if max_students > 0 or (not dp_prev and bin(arrangement).count('1') > 0):
                    dp[i][arrangement] = max_students + bin(arrangement).count('1')

        if dp[-1]:
            return max(dp[-1].values())
        return 0