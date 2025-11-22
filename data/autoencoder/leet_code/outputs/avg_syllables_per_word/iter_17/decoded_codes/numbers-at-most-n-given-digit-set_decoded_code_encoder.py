class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        def count_numbers_with_length(length):
            return len(digits) ** length

        def count_numbers_up_to_n(n):
            string_n = str(n)
            length = len(string_n)
            count = 0

            # Count numbers with length less than n's length
            for l in range(1, length):
                count += count_numbers_with_length(l)

            for i in range(length):
                current_digit = int(string_n[i])
                for digit in digits:
                    digit_value = int(digit)
                    if digit_value < current_digit:
                        count += count_numbers_with_length(length - i - 1)
                    elif digit_value == current_digit:
                        if i == length - 1:
                            count += 1
                    else:
                        break
                else:
                    continue
                if digit_value > current_digit:
                    break

            return count

        return count_numbers_up_to_n(n)