class Solution:
    def numberOfWays(self, corridor: str) -> int:
        MODULO = 10**9 + 7
        seats = [index for index, character in enumerate(corridor) if character == 'S']

        if len(seats) % 2 != 0 or len(seats) < 2:
            return 0

        ways = 1
        for i in range(2, len(seats), 2):
            ways = (ways * (seats[i] - seats[i - 1])) % MODULO

        return ways