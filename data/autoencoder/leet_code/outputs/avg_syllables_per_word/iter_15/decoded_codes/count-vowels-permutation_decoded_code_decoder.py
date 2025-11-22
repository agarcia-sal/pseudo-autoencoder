class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10**9 + 7
        a = e = i = o = u = 1
        for _ in range(2, n + 1):
            a_next = e + i + u
            e_next = a + i
            i_next = e + o
            o_next = i
            u_next = i + o
            a = a_next % MOD
            e = e_next % MOD
            i = i_next % MOD
            o = o_next % MOD
            u = u_next % MOD
        total_sum = a + e + i + o + u
        result = total_sum % MOD
        return result