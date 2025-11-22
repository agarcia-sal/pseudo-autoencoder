class Solution:
    def nthMagicalNumber(self, n, a, b):
        MOD = 10**9 + 7

        def gcd(x, y):
            while y != 0:
                temp_x = y
                temp_y = x % y
                x = temp_x
                y = temp_y
            return x

        def lcm(x, y):
            return x * y // gcd(x, y)

        L = lcm(a, b)
        left = 1
        right = n * min(a, b)

        while left < right:
            mid = (left + right) // 2
            count = mid // a + mid // b - mid // L

            if count < n:
                left = mid + 1
            else:
                right = mid

        return left % MOD