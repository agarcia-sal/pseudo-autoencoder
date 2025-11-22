class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        MODULO_DIVISOR = 10**9 + 7

        if primeFactors <= 3:
            return primeFactors

        number_of_threes = primeFactors // 3
        remainder_after_division = primeFactors % 3

        if remainder_after_division == 0:
            return pow(3, number_of_threes, MODULO_DIVISOR)
        elif remainder_after_division == 1:
            # Adjust by converting one "3 + 1" into "2 + 2" to maximize product
            return (pow(3, number_of_threes - 1, MODULO_DIVISOR) * 4) % MODULO_DIVISOR
        else:
            # remainder_after_division == 2
            return (pow(3, number_of_threes, MODULO_DIVISOR) * 2) % MODULO_DIVISOR