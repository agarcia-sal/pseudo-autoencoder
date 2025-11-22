class Solution:
    def digitsCount(self, digit: int, low: int, high: int) -> int:
        def count_digit(number: int, target_digit: int) -> int:
            count = 0
            power_of_ten = 1
            current = number
            while current > 0:
                last = current % 10
                current //= 10
                full_cycles = current
                if target_digit == 0:
                    full_cycles -= 1
                    if full_cycles < 0:
                        full_cycles = 0
                count += full_cycles * power_of_ten
                if last > target_digit:
                    count += power_of_ten
                elif last == target_digit:
                    count += (number % power_of_ten) + 1
                power_of_ten *= 10
            return count

        if low > high:
            return 0
        if digit < 0 or digit > 9:
            return 0

        return count_digit(high, digit) - count_digit(low - 1, digit)