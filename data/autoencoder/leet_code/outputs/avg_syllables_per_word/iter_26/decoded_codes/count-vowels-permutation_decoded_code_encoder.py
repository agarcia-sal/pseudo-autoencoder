class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MODULO = 10**9 + 1

        count_a = 1
        count_e = 1
        count_i = 1
        count_o = 1
        count_u = 1

        for _ in range(2, n + 1):
            next_count_a = count_e + count_i + count_u
            next_count_e = count_a + count_i
            next_count_i = count_e + count_o
            next_count_o = count_i
            next_count_u = count_i + count_o

            count_a = next_count_a % MODULO
            count_e = next_count_e % MODULO
            count_i = next_count_i % MODULO
            count_o = next_count_o % MODULO
            count_u = next_count_u % MODULO

        total_count = count_a + count_e + count_i + count_o + count_u
        return total_count % MODULO