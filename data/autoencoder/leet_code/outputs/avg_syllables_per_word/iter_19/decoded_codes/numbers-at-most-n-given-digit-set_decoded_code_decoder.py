from bisect import bisect_left

class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        digits_int = sorted(int(d) for d in digits)

        def count_numbers_with_length(length):
            return len(digits_int) ** length

        def count_numbers_up_to_n(n):
            s = str(n)
            length = len(s)
            count = 0

            # Count all numbers with lengths less than length of n
            for l in range(1, length):
                count += count_numbers_with_length(l)

            for i in range(length):
                current_digit = int(s[i])
                smaller_digits_count = bisect_left(digits_int, current_digit)
                power = length - i - 1
                count += smaller_digits_count * (len(digits_int) ** power)

                if current_digit not in digits_int:
                    return count  # no exact match continuation possible

            # If we reach here, all digits matched exactly
            return count + 1

        return count_numbers_up_to_n(n)