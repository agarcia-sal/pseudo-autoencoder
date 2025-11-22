class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MODULO_DIVISOR = 10**9 + 7
        count_of_a = 1
        count_of_e = 1
        count_of_i = 1
        count_of_o = 1
        count_of_u = 1

        for _ in range(2, n + 1):
            next_count_of_a = count_of_e + count_of_i + count_of_u
            next_count_of_e = count_of_a + count_of_i
            next_count_of_i = count_of_e + count_of_o
            next_count_of_o = count_of_i
            next_count_of_u = count_of_i + count_of_o

            count_of_a = next_count_of_a % MODULO_DIVISOR
            count_of_e = next_count_of_e % MODULO_DIVISOR
            count_of_i = next_count_of_i % MODULO_DIVISOR
            count_of_o = next_count_of_o % MODULO_DIVISOR
            count_of_u = next_count_of_u % MODULO_DIVISOR

        total_count = count_of_a + count_of_e + count_of_i + count_of_o + count_of_u
        result = total_count % MODULO_DIVISOR
        return result