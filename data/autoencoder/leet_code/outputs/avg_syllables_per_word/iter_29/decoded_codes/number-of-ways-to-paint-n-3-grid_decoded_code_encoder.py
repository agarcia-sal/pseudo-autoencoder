class Solution:
    def numOfWays(self, n: int) -> int:
        MODULO_VALUE = 10**9 + 7
        count_type_a = 6
        count_type_b = 6
        for _ in range(2, n + 1):
            new_count_type_a = (count_type_a * 3 + count_type_b * 2) % MODULO_VALUE
            new_count_type_b = (count_type_a * 2 + count_type_b * 2) % MODULO_VALUE
            count_type_a, count_type_b = new_count_type_a, new_count_type_b
        total_count = (count_type_a + count_type_b) % MODULO_VALUE
        return total_count