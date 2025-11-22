from typing import List

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seats = [i for i, c in enumerate(corridor) if c == 'S']

        # If number of seats is not even or less than 2, no valid ways exist
        if len(seats) % 2 != 0 or len(seats) < 2:
            return 0

        ways = 1
        # Iterate over every pair of seats starting from the second pair
        for i in range(2, len(seats), 2):
            seat_distance = seats[i] - seats[i - 1]
            ways = (ways * seat_distance) % MOD

        return ways