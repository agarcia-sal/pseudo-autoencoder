class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        digits = sorted(digits)  # Ensure digits are in ascending order for correct comparison

        def count_numbers_with_length(length):
            return len(digits) ** length

        def count_numbers_up_to_n(n):
            string_n = str(n)
            length = len(string_n)
            count = 0

            for l in range(1, length):
                count += count_numbers_with_length(l)

            for i in range(length):
                current_digit = int(string_n[i])
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