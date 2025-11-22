from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        def count_numbers_with_length(length: int) -> int:
            return len(digits) ** length

        def count_numbers_up_to_n(n: int) -> int:
            string_n = str(n)
            length = len(string_n)
            count = 0

            for l in range(1, length):
                count += count_numbers_with_length(l)

            for i in range(length):
                current_digit = int(string_n[i])
                found_equal = False
                for d in digits:
                    digit_value = int(d)
                    if digit_value < current_digit:
                        count += count_numbers_with_length(length - i - 1)
                    elif digit_value == current_digit:
                        found_equal = True
                        if i == length - 1:
                            count += 1
                        break
                    else:
                        break
                if not found_equal:
                    break

            return count

        return count_numbers_up_to_n(n)