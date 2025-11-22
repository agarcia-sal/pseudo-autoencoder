class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        limit = int(n ** 0.5)
        for start in range(2, limit + 1):
            if is_prime[start]:
                for multiple in range(start * start, n, start):
                    is_prime[multiple] = False

        prime_count = sum(is_prime)
        return prime_count