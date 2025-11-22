class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MODULO = 10**9 + 7
        count_of_a = 1
        count_of_e = 1
        count_of_i = 1
        count_of_o = 1
        count_of_u = 1
        for _ in range(2, n + 1):
            next_count_of_a = (count_of_e + count_of_i + count_of_u) % MODULO
            next_count_of_e = (count_of_a + count_of_i) % MODULO
            next_count_of_i = (count_of_e + count_of_o) % MODULO
            next_count_of_o = count_of_i % MODULO
            next_count_of_u = (count_of_i + count_of_o) % MODULO
            count_of_a = next_count_of_a
            count_of_e = next_count_of_e
            count_of_i = next_count_of_i
            count_of_o = next_count_of_o
            count_of_u = next_count_of_u
        total_count = (count_of_a + count_of_e + count_of_i + count_of_o + count_of_u) % MODULO
        return total_count