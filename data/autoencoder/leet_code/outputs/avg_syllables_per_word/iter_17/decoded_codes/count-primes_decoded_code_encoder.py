from math import isqrt
from typing import List

class Solution:
    def countPrimes(self, number_n: int) -> int:
        if number_n <= 2:
            return 0

        def InitializeListOfBoolean(n: int) -> List[bool]:
            return [True] * n

        def IntegerSquareRoot(n: int) -> int:
            return isqrt(n)

        def SumBooleanList(lst: List[bool]) -> int:
            return sum(lst)

        list_is_prime = InitializeListOfBoolean(number_n)
        list_is_prime[0] = False
        list_is_prime[1] = False

        for start in range(2, IntegerSquareRoot(number_n) + 1):
            if list_is_prime[start]:
                for multiple in range(start * start, number_n, start):
                    list_is_prime[multiple] = False

        return SumBooleanList(list_is_prime)