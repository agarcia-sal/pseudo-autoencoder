from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        def count_numbers_with_length(length: int) -> int:
            return len(digits) ** length

        def count_numbers_up_to_n(n: int) -> int:
            str_n = str(n)
            length = len(str_n)
            count = 0

            # Count numbers with length less than 'length'
            for l in range(1, length):
                count += count_numbers_with_length(l)

            # Count numbers with length equal to 'length'
            for i in range(length):
                current_digit = int(str_n[i])
                digit_found = False
                for digit in digits:
                    digit_value = int(digit)
                    if digit_value < current_digit:
                        count += count_numbers_with_length(length - i - 1)
                    elif digit_value == current_digit:
                        if i == length - 1:
                            count += 1
                        digit_found = True
                        break
                    else:
                        break
                if not digit_found:
                    break

            return count

        return count_numbers_up_to_n(n)