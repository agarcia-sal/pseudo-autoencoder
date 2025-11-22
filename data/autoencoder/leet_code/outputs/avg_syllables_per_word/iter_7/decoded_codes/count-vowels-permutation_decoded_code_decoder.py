from typing import ClassVar

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD: ClassVar[int] = 10**9 + 7
        a = e = i = o = u = 1
        for _ in range(1, n):
            a_next = (e + i + u) % MOD
            e_next = (a + i) % MOD
            i_next = (e + o) % MOD
            o_next = i % MOD
            u_next = (i + o) % MOD
            a, e, i, o, u = a_next, e_next, i_next, o_next, u_next
        return (a + e + i + o + u) % MOD