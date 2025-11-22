class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def count_digit(n: int, digit: int) -> int:
            if n < 0:
                return 0
            count = 0
            power_of_10 = 1
            current = n
            while current > 0:
                last = current % 10
                current //= 10
                full_cycles = current
                if digit == 0:
                    full_cycles -= 1
                count += full_cycles * power_of_10
                if last > digit:
                    count += power_of_10
                elif last == digit:
                    count += (n % power_of_10) + 1
                power_of_10 *= 10
            # special case: if digit == 0 and n > 0, we need to count the zero at 0 itself
            if digit == 0 and n >= 0:
                count += 1
            return count

        return count_digit(high, d) - count_digit(low - 1, d)