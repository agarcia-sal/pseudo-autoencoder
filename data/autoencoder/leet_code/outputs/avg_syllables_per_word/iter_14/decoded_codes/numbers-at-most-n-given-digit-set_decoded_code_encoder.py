class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        def count_numbers_with_length(length):
            return len(digits) ** length

        def count_numbers_up_to_n(n):
            str_n = str(n)
            length = len(str_n)
            count = 0

            # Count numbers with lengths less than length of n
            for l in range(1, length):
                count += count_numbers_with_length(l)

            for i in range(length):
                current_digit = int(str_n[i])
                found_equal = False
                for digit in digits:
                    digit_value = int(digit)
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