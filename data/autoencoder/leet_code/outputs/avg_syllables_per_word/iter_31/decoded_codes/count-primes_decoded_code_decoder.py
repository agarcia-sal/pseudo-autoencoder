from math import isqrt
from typing import List

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime: List[bool] = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        limit = isqrt(n) + 1
        for start in range(2, limit):
            if is_prime[start]:
                for multiple in range(start * start, n, start):
                    is_prime[multiple] = False

        return sum(is_prime)