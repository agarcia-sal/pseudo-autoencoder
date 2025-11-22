class Solution:
    def minSteps(self, n: int) -> int:
        # If n is 1, no steps are required
        if n == 1:
            return 0

        operations = 0
        factor = 2

        # Factorize n and accumulate the sum of factors
        while n > 1:
            while n % factor == 0:
                operations += factor
                n //= factor
            factor += 1

        return operations