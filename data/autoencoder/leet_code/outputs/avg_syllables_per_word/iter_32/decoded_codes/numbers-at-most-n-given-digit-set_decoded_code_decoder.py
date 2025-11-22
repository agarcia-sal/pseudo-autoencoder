from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        def count_numbers_with_length(length: int) -> int:
            # Number of numbers of given length that can be formed using digits
            return len(digits) ** length

        def count_numbers_up_to_n(n_val: int) -> int:
            str_n = str(n_val)
            length = len(str_n)
            count = 0

            # Count all numbers with length less than 'length'
            for l in range(1, length):
                count += count_numbers_with_length(l)

            # Count numbers with the same length
            for i in range(length):
                current_digit = int(str_n[i])
                has_equal = False
                for d in digits:
                    digit_value = int(d)
                    if digit_value < current_digit:
                        count += count_numbers_with_length(length - i - 1)
                    elif digit_value == current_digit:
                        has_equal = True
                        if i == length - 1:
                            count += 1  # Number itself is counted
                        break
                    else:
                        break
                if not has_equal:
                    # Cannot continue forming valid numbers if no matching digit found
                    break
            return count

        return count_numbers_up_to_n(n)