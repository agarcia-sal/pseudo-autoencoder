class Solution:
    def isSolvable(self, words, result):
        unique_chars = set(''.join(words) + result)
        if len(unique_chars) > 10:
            return False

        non_zero_chars = {word[0] for word in words if len(word) > 1}
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

        def backtrack(index, col, sum_col):
            max_word_length = max(len(word) for word in words)
            if col >= max_word_length and col >= len(result):
                return sum_col == 0

            if index == len(words):
                if col < len(result):
                    digit_char = result[len(result) - 1 - col]
                    digit_needed = sum_col % 10
                    if digit_char in char_to_digit:
                        if char_to_digit[digit_char] == digit_needed:
                            return backtrack(0, col + 1, sum_col // 10)
                        else:
                            return False
                    else:
                        if can_assign(digit_char, digit_needed) and (digit_needed != 0 or digit_char not in non_zero_chars):
                            assign(digit_char, digit_needed)
                            if backtrack(0, col + 1, sum_col // 10):
                                return True
                            unassign(digit_char, digit_needed)
                else:
                    return sum_col == 0
                return False

            current_word = words[index]
            if col >= len(current_word):
                return backtrack(index + 1, col, sum_col)

            current_char = current_word[len(current_word) - 1 - col]
            if current_char in char_to_digit:
                return backtrack(index + 1, col, sum_col + char_to_digit[current_char])
            else:
                for digit in range(10):
                    if can_assign(current_char, digit) and (digit != 0 or current_char not in non_zero_chars):
                        assign(current_char, digit)
                        if backtrack(index + 1, col, sum_col + digit):
                            return True
                        unassign(current_char, digit)
                return False

        return backtrack(0, 0, 0)