class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MODULO = 10**9 + 7
        count_a = count_e = count_i = count_o = count_u = 1

        for _ in range(1, n):
            next_a = count_e + count_i + count_u
            next_e = count_a + count_i
            next_i = count_e + count_o
            next_o = count_i
            next_u = count_i + count_o

            count_a = next_a % MODULO
            count_e = next_e % MODULO
            count_i = next_i % MODULO
            count_o = next_o % MODULO
            count_u = next_u % MODULO

        total = count_a + count_e + count_i + count_o + count_u
        return total % MODULO