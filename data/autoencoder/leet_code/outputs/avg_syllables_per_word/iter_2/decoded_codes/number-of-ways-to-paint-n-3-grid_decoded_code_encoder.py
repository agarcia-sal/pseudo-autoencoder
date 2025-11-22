class Solution:
    def numOfWays(self, n):
        MOD = 10**9 + 7
        a = 6
        b = 6
        for index in range(2, n + 1):
            new_a = (3 * a + 2 * b) % MOD
            new_b = (2 * a + 2 * b) % MOD
            a = new_a
            b = new_b
        return (a + b) % MOD