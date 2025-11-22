class Solution:
    def digitsCount(self, D: int, LOW: int, HIGH: int) -> int:
        def count_digit(N: int, DIGIT: int) -> int:
            count = 0
            power_of_ten = 1
            current_value = N
            while current_value > 0:
                last_digit = current_value % 10
                current_value //= 10
                full_cycles = current_value
                if DIGIT == 0:
                    full_cycles -= 1
                count += full_cycles * power_of_ten
                if last_digit > DIGIT:
                    count += power_of_ten
                elif last_digit == DIGIT:
                    count += N % power_of_ten + 1
                power_of_ten *= 10
            return count

        return count_digit(HIGH, D) - count_digit(LOW - 1, D)