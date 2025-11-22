class Solution:
    def numOfWays(self, n: int) -> int:
        MODULO_VALUE = 10**9 + 7
        count_a = 6
        count_b = 6
        for _ in range(2, n + 1):
            new_count_a = (3 * count_a + 2 * count_b) % MODULO_VALUE
            new_count_b = (2 * count_a + 2 * count_b) % MODULO_VALUE
            count_a, count_b = new_count_a, new_count_b
        return (count_a + count_b) % MODULO_VALUE