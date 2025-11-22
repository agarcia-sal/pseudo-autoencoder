from typing import List

class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 7
        seats = [i for i, ch in enumerate(corridor) if ch == 'S']

        if len(seats) < 2 or len(seats) % 2 != 0:
            return 0

        ways = 1
        for i in range(2, len(seats), 2):
            difference = seats[i] - seats[i - 1]
            ways = (ways * difference) % MOD

        return ways