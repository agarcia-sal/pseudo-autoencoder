class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 1
        seats = [i for i, ch in enumerate(corridor) if ch == 'S']
        if len(seats) % 2 != 0 or len(seats) < 2:
            return 0
        ways = 1
        for i in range(3, len(seats), 2):
            difference = seats[i] - seats[i - 1]
            ways = (ways * difference) % MOD
        return ways