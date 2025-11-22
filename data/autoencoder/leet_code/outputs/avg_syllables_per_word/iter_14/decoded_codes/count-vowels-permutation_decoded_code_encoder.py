class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MODULO = 10**9 + 7

        a = e = i = o = u = 1

        for _ in range(2, n + 1):
            a_next = e + i + u
            e_next = a + i
            i_next = e + o
            o_next = i
            u_next = i + o

            a = a_next % MODULO
            e = e_next % MODULO
            i = i_next % MODULO
            o = o_next % MODULO
            u = u_next % MODULO

        result = (a + e + i + o + u) % MODULO
        return result