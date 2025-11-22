class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10**9 + 1
        seats = [i for i, x in enumerate(corridor) if x == 'S']
        if len(seats) < 2 or len(seats) % 2 != 0:
            return 0
        ways = 1
        for i in range(2, len(seats), 2):
            ways = (ways * (seats[i] - seats[i - 1])) % MOD
        return ways