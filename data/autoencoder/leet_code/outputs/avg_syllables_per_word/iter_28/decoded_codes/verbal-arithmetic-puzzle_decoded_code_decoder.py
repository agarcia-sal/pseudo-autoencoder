from typing import List

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        unique_chars = set(''.join(words) + result)
        if len(unique_chars) > 10:
            return False

        non_zero_chars = {word[0] for word in words if len(word) > 1}
        if len(result) > 1:
            non_zero_chars.add(result[0])

        char_to_digit = {}
        digit_to_char = {}

        def can_assign(char: str, digit: int) -> bool:
            return char not in char_to_digit and (digit not in digit_to_char or digit_to_char[digit] == char)

        def assign(char: str, digit: int) -> None:
            char_to_digit[char] = digit
            digit_to_char[digit] = char

        def unassign(char: str, digit: int) -> None:
            char_to_digit.pop(char, None)
            digit_to_char.pop(digit, None)

        max_word_length = max(map(len, words)) if words else 0

        def backtrack(index: int, column: int, sum_column: int) -> bool:
            if column >= max_word_length and column >= len(result):
                return sum_column == 0

            if index == len(words):
                if column < len(result):
                    current_char = result[-1 - column]
                    mod_digit = sum_column % 10
                    if current_char in char_to_digit:
                        if char_to_digit[current_char] == mod_digit:
                            return backtrack(0, column + 1, sum_column // 10)
                        return False
                    else:
                        if can_assign(current_char, mod_digit) and (mod_digit != 0 or current_char not in non_zero_chars):
                            assign(current_char, mod_digit)
                            if backtrack(0, column + 1, sum_column // 10):
                                return True
                            unassign(current_char, mod_digit)
                        return False
                else:
                    return sum_column == 0

            current_word = words[index]
            if column >= len(current_word):
                return backtrack(index + 1, column, sum_column)

            current_char = current_word[-1 - column]
            if current_char in char_to_digit:
                return backtrack(index + 1, column, sum_column + char_to_digit[current_char])

            for digit in range(10):
                if can_assign(current_char, digit) and (digit != 0 or current_char not in non_zero_chars):
                    assign(current_char, digit)
                    if backtrack(index + 1, column, sum_column + digit):
                        return True
                    unassign(current_char, digit)

            return False

        return backtrack(0, 0, 0)