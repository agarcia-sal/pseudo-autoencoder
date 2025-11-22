class Solution:
    def numOfWays(self, n: int) -> int:
        MODULO = 10**9 + 7
        a = 6
        b = 6
        for _ in range(2, n + 1):
            temporary_a = (3 * a + 2 * b) % MODULO
            temporary_b = (2 * a + 2 * b) % MODULO
            a = temporary_a
            b = temporary_b
        result = (a + b) % MODULO
        return result