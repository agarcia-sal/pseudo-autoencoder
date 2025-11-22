class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        def count_numbers_with_length(length):
            return len(digits) ** length

        def count_numbers_up_to_n(n):
            s = str(n)
            length_n = len(s)
            total_count = 0

            for length_index in range(1, length_n):
                total_count += count_numbers_with_length(length_index)

            for digit_index in range(length_n):
                current_digit = int(s[digit_index])
                for digit in digits:
                    digit_value = int(digit)
                    if digit_value < current_digit:
                        total_count += count_numbers_with_length(length_n - digit_index - 1)
                    elif digit_value == current_digit:
                        if digit_index == length_n - 1:
                            total_count += 1
                        break
                    else:
                        break

            return total_count

        return count_numbers_up_to_n(n)