from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits_sorted = sorted(digits, key=int)  # ensure digits are sorted numerically

        def count_numbers_with_length(length: int) -> int:
            return len(digits_sorted) ** length

        def count_numbers_up_to_n(num: int) -> int:
            s = str(num)
            length = len(s)
            total_count = 0

            # Count numbers with lengths less than length of s
            for l in range(1, length):
                total_count += count_numbers_with_length(l)

            # Count numbers with the same length as s
            for i in range(length):
                current_digit = int(s[i])
                for d in digits_sorted:
                    digit_value = int(d)
                    if digit_value < current_digit:
                        # For each smaller digit, add numbers formed by remaining positions
                        total_count += count_numbers_with_length(length - i - 1)
                    elif digit_value == current_digit:
                        # If equal, continue to next digit if not last, else add 1
                        if i == length - 1:
                            total_count += 1
                        break
                    else:
                        # digit_value > current_digit; stop checking higher digits
                        break

            return total_count

        return count_numbers_up_to_n(n)