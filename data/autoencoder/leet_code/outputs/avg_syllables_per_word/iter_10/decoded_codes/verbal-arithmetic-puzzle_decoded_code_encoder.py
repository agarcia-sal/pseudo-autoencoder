class Solution:
    def isSolvable(self, words, result):
        unique_chars = set(''.join(words) + result)
        if len(unique_chars) > 10:
            return False

        non_zero_chars = {w[0] for w in words if len(w) > 1}
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

        max_len = max(max(len(w) for w in words), len(result))

        def backtrack(index, col, sum_col):
            if col >= max_len:
                return sum_col == 0

            if index == len(words):
                if col < len(result):
                    digit_char = result[len(result) - 1 - col]
                    expected_digit = sum_col % 10
                    if digit_char in char_to_digit:
                        if char_to_digit[digit_char] == expected_digit:
                            return backtrack(0, col + 1, sum_col // 10)
                        return False
                    else:
                        if can_assign(digit_char, expected_digit) and (expected_digit != 0 or digit_char not in non_zero_chars):
                            assign(digit_char, expected_digit)
                            if backtrack(0, col + 1, sum_col // 10):
                                return True
                            unassign(digit_char, expected_digit)
                        return False
                else:
                    return sum_col == 0

            current_word = words[index]
            if col >= len(current_word):
                return backtrack(index + 1, col, sum_col)

            current_char = current_word[len(current_word) - 1 - col]
            if current_char in char_to_digit:
                return backtrack(index + 1, col, sum_col + char_to_digit[current_char])

            for digit in range(10):
                if can_assign(current_char, digit) and (digit != 0 or current_char not in non_zero_chars):
                    assign(current_char, digit)
                    if backtrack(index + 1, col, sum_col + digit):
                        return True
                    unassign(current_char, digit)

            return False

        return backtrack(0, 0, 0)