from bisect import bisect_left

class Solution:
    def atMostNGivenDigitSet(self, digits: list[str], n: int) -> int:
        digits_int = sorted(int(d) for d in digits)
        digits_len = len(digits_int)

        def count_numbers_with_length(length: int) -> int:
            return digits_len ** length

        def count_numbers_up_to_n(n: int) -> int:
            str_n = str(n)
            length = len(str_n)
            count = 0

            # Count numbers with length less than length of n
            for l in range(1, length):
                count += count_numbers_with_length(l)

            # Count numbers with length equal to length of n, digit by digit
            for i in range(length):
                current_digit = int(str_n[i])
                for digit_value in digits_int:
                    if digit_value < current_digit:
                        count += count_numbers_with_length(length - i - 1)
                    elif digit_value == current_digit:
                        if i == length - 1:
                            count += 1
                        break
                    else:
                        break
            return count

        return count_numbers_up_to_n(n)