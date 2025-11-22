class Solution:
    def digitsCount(self, d: int, low: int, high: int) -> int:
        def count_digit(n: int, digit: int) -> int:
            count = 0
            power_of_ten = 1
            current = n
            while current > 0:
                last = current % 10
                current //= 10
                full_cycles = current
                if digit == 0:
                    full_cycles -= 1
                count += full_cycles * power_of_ten
                if last > digit:
                    count += power_of_ten
                elif last == digit:
                    count += (n % power_of_ten) + 1
                power_of_ten *= 10
            return max(count, 0)  # to avoid negative counts especially when n < 0

        return count_digit(high, d) - count_digit(low - 1, d)