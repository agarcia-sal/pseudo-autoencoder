class Solution:
    def numOfWays(self, n: int) -> int:
        MODULO_VALUE = 10**9 + 7

        a = 6
        b = 6

        for _ in range(2, n + 1):
            temp_a = 3 * a + 2 * b
            temp_b = 2 * a + 2 * b
            a = temp_a % MODULO_VALUE
            b = temp_b % MODULO_VALUE

        result = (a + b) % MODULO_VALUE
        return result