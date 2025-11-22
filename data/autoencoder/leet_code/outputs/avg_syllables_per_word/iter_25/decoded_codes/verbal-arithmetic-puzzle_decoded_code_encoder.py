class Solution:
    def isSolvable(self, words, result):
        unique_chars = set(''.join(words) + result)
        if len(unique_chars) > 10:
            return False

        non_zero_chars = set(word[0] for word in words if len(word) > 1)
        if len(result) > 1:
            non_zero_chars.add(result[0])

        char_to_digit = {}
        digit_to_char = {}

        def can_assign(char, digit):
            return char not in char_to_digit and (digit not in digit_to_char or digit_to_char[digit] == char)

        def assign(char, digit):
            char_to_digit[char] = digit
            digit_to_char[digit] = char

        def unassign(char, digit):
            del char_to_digit[char]
            del digit_to_char[digit]

        def word_value(word):
            total_value = 0
            for i, char in enumerate(reversed(word)):
                total_value += char_to_digit[char] * (10 ** i)
            return total_value

        max_len = max(max(len(word) for word in words), len(result))

        def backtrack(index, col, sum_col):
            if col >= max_len:
                # All columns processed
                return sum_col == 0

            if index == len(words):
                if col < len(result):
                    digit_char = result[len(result) - 1 - col]
                    if digit_char in char_to_digit:
                        if char_to_digit[digit_char] == sum_col % 10:
                            return backtrack(0, col + 1, sum_col // 10)
                        else:
                            return False
                    else:
                        digit_val = sum_col % 10
                        # leading zero check
                        if can_assign(digit_char, digit_val) and (digit_val != 0 or digit_char not in non_zero_chars):
                            assign(digit_char, digit_val)
                            if backtrack(0, col + 1, sum_col // 10):
                                return True
                            unassign(digit_char, digit_val)
                else:
                    return sum_col == 0
                return False

            word = words[index]
            if col >= len(word):
                return backtrack(index + 1, col, sum_col)

            char = word[len(word) - 1 - col]
            if char in char_to_digit:
                return backtrack(index + 1, col, sum_col + char_to_digit[char])

            for digit in range(10):
                if can_assign(char, digit) and (digit != 0 or char not in non_zero_chars):
                    assign(char, digit)
                    if backtrack(index + 1, col, sum_col + digit):
                        return True
                    unassign(char, digit)

            return False

        return backtrack(0, 0, 0)