class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MODULO = 10**9 + 7

        if primeFactors <= 3:
            return primeFactors

        number_of_threes = primeFactors // 3
        remainder_after_division = primeFactors % 3

        if remainder_after_division == 0:
            return pow(3, number_of_threes, MODULO)
        elif remainder_after_division == 1:
            return (pow(3, number_of_threes - 1, MODULO) * 4) % MODULO
        else:  # remainder_after_division == 2
            return (pow(3, number_of_threes, MODULO) * 2) % MODULO