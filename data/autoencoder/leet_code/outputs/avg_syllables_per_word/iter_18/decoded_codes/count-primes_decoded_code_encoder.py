import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False
        limit = int(math.isqrt(n))
        for start in range(2, limit + 1):
            if is_prime[start]:
                for multiple in range(start * start, n, start):
                    is_prime[multiple] = False
        return sum(is_prime)