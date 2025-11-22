class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        operations = 0
        factor = 2
        while n > 1 and factor * factor <= n:
            while n % factor == 0:
                operations += factor
                n //= factor
            factor += 1
        if n > 1:
            operations += n
        return operations