from typing import List

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        def count_numbers_with_length(length: int) -> int:
            # Count how many numbers can be formed with given digits of specified length
            return len(digits) ** length

        def count_numbers_up_to_n(n: int) -> int:
            s = str(n)
            length = len(s)
            count = 0

            # Count all numbers with length less than length of n
            for l in range(1, length):
                count += count_numbers_with_length(l)

            # Count numbers with the same length
            for i in range(length):
                current_digit = int(s[i])
                has_equal_digit = False
                for d in digits:
                    d_int = int(d)
                    if d_int < current_digit:
                        count += count_numbers_with_length(length - i - 1)
                    elif d_int == current_digit:
                        has_equal_digit = True
                        if i == length - 1:
                            count += 1
                        break
                    else:
                        break
                if not has_equal_digit:
                    break

            return count

        return count_numbers_up_to_n(n)