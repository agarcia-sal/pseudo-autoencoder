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
                multiple = start * start
                while multiple < n:
                    is_prime[multiple] = False
                    multiple += start
        count = 0
        for value in is_prime:
            if value:
                count += 1
        return count