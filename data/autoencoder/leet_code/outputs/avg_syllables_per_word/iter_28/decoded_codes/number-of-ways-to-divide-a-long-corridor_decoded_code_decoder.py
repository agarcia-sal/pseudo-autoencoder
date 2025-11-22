from typing import List

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seats: List[int] = []
        for i, x in enumerate(corridor):
            if x == 'S':
                seats.append(i)
        if len(seats) < 2 or len(seats) % 2 != 0:
            return 0
        ways = 1
        for i in range(2, len(seats), 2):
            difference = seats[i] - seats[i-1]
            ways = (ways * difference) % MOD
        return ways