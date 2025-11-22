class Solution:
    def atMostNGivenDigitSet(self, digits, n):
        def count_numbers_with_length(length):
            return len(digits) ** length

        def count_numbers_up_to_n(n):
            str_n = str(n)
            length = len(str_n)
            count = 0

            # Count numbers with length less than that of n
            for length_iterator in range(1, length):
                count += count_numbers_with_length(length_iterator)

            # Count numbers with the same length as n
            for index in range(length):
                current_digit = int(str_n[index])
                for digit in digits:
                    digit_value = int(digit)
                    if digit_value < current_digit:
                        count += count_numbers_with_length(length - index - 1)
                    elif digit_value == current_digit:
                        if index == length - 1:
                            count += 1
                    else:
                        break
                else:
                    # Continue outer loop only if break was not called
                    continue
                # Break outer loop if inner loop was broken
                break

            return count

        return count_numbers_up_to_n(n)