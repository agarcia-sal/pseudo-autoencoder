class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MOD = 10**9 + 1

        if primeFactors <= 3:
            return primeFactors

        num_threes = primeFactors // 3
        remainder = primeFactors - num_threes * 3

        if remainder == 0:
            return pow(3, num_threes, MOD)
        elif remainder == 1:
            # Adjust using (3^(num_threes-1)) * 4 mod MOD
            return (pow(3, num_threes - 1, MOD) * 4) % MOD
        else:
            # remainder == 2
            return (pow(3, num_threes, MOD) * 2) % MOD