class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MOD = 10**9 + 7

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def lcm(x, y):
            return x // gcd(x, y) * y

        L = lcm(a, b)
        left, right = 1, n * min(a, b)

        while left < right:
            mid = (left + right) // 2
            count = mid // a + mid // b - mid // L
            if count < n:
                left = mid + 1
            else:
                right = mid

        return left % MOD