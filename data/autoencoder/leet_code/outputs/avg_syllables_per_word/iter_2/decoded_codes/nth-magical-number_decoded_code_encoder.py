class Solution:
    def nthMagicalNumber(self, n, a, b):
        MOD = 1000000007

        def gcd(x, y):
            while y != 0:
                temp = y
                y = x % y
                x = temp
            return x

        def lcm(x, y):
            return x * y // gcd(x, y)

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