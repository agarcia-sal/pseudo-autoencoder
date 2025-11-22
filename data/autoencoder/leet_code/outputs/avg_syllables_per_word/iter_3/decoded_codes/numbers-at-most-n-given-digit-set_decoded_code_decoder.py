class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        digits = sorted(digits)

        def count_numbers_with_length(length):
            return len(digits) ** length

        def count_numbers_up_to_n(n):
            str_n = str(n)
            length = len(str_n)
            count = 0

            for l in range(1, length):
                count += count_numbers_with_length(l)

            for i in range(length):
                current_digit = int(str_n[i])
                has_equal_digit = False

                for d in digits:
                    digit_value = int(d)
                    if digit_value < current_digit:
                        count += count_numbers_with_length(length - i - 1)
                    elif digit_value == current_digit:
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