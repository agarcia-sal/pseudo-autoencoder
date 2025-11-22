class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        MODULO_CONSTANT = 10**9 + 7

        def gcd(x: int, y: int) -> int:
            while y != 0:
                x, y = y, x % y
            return x

        def lcm(x: int, y: int) -> int:
            return x * y // gcd(x, y)

        LCM_VALUE = lcm(a, b)

        left_bound, right_bound = 1, n * min(a, b)

        while left_bound < right_bound:
            middle_point = (left_bound + right_bound) // 2
            count_of_magical_numbers = (middle_point // a) + (middle_point // b) - (middle_point // LCM_VALUE)

            if count_of_magical_numbers < n:
                left_bound = middle_point + 1
            else:
                right_bound = middle_point

        return left_bound % MODULO_CONSTANT