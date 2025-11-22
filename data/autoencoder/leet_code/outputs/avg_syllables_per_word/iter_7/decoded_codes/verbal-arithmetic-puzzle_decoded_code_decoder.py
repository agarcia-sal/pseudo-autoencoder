from typing import List

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        unique_chars = set(''.join(words) + result)
        if len(unique_chars) > 10:
            return False

        non_zero_chars = {w[0] for w in words if len(w) > 1}
        if len(result) > 1:
            non_zero_chars.add(result[0])

        char_to_digit = {}
        digit_to_char = {}

        def can_assign(char: str, digit: int) -> bool:
            return (char not in char_to_digit) and (digit not in digit_to_char or digit_to_char[digit] == char)

        def assign(char: str, digit: int):
            char_to_digit[char] = digit
            digit_to_char[digit] = char

        def unassign(char: str, digit: int):
            char_to_digit.pop(char)
            digit_to_char.pop(digit)

        def backtrack(index: int, col: int, sum_col: int) -> bool:
            max_len = max(map(len, words))
            if col >= max_len and col >= len(result):
                return sum_col == 0

            if index == len(words):
                if col < len(result):
                    digit_char = result[len(result) - 1 - col]
                    d = sum_col % 10
                    if digit_char in char_to_digit:
                        if char_to_digit[digit_char] == d:
                            return backtrack(0, col + 1, sum_col // 10)
                        else:
                            return False
                    else:
                        if can_assign(digit_char, d) and (d != 0 or digit_char not in non_zero_chars):
                            assign(digit_char, d)
                            if backtrack(0, col + 1, sum_col // 10):
                                return True
                            unassign(digit_char, d)
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