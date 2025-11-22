from typing import List, Dict, Set

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        unique_chars: Set[str] = set(''.join(words) + result)
        if len(unique_chars) > 10:
            return False

        non_zero_chars: Set[str] = set()
        for w in words:
            if len(w) > 1:
                non_zero_chars.add(w[0])
        if len(result) > 1:
            non_zero_chars.add(result[0])

        char_to_digit: Dict[str, int] = {}
        digit_to_char: Dict[int, str] = {}

        def can_assign(char: str, digit: int) -> bool:
            return char not in char_to_digit and (digit not in digit_to_char or digit_to_char[digit] == char)

        def assign(char: str, digit: int) -> None:
            char_to_digit[char] = digit
            digit_to_char[digit] = char

        def unassign(char: str, digit: int) -> None:
            char_to_digit.pop(char)
            digit_to_char.pop(digit)

        def word_value(word: str) -> int:
            value = 0
            length = len(word)
            for pos in range(length):
                c = word[length - 1 - pos]
                value += char_to_digit[c] * (10 ** pos)
            return value

        max_word_length = max((len(w) for w in words), default=0)

        def backtrack(index: int, col: int, sum_col: int) -> bool:
            if col >= max_word_length and col >= len(result):
                return sum_col == 0

            if index == len(words):
                if col < len(result):
                    digit_char = result[len(result) - 1 - col]
                    digit_expected = sum_col % 10
                    if digit_char in char_to_digit:
                        if char_to_digit[digit_char] == digit_expected:
                            return backtrack(0, col + 1, sum_col // 10)
                        else:
                            return False
                    else:
                        if (digit_expected != 0 or digit_char not in non_zero_chars) and can_assign(digit_char, digit_expected):
                            assign(digit_char, digit_expected)
                            if backtrack(0, col + 1, sum_col // 10):
                                return True
                            unassign(digit_char, digit_expected)
                else:
                    return sum_col == 0
                return False

            current_word = words[index]
            if col >= len(current_word):
                return backtrack(index + 1, col, sum_col)

            current_char = current_word[len(current_word) - 1 - col]
            if current_char in char_to_digit:
                return backtrack(index + 1, col, sum_col + char_to_digit[current_char])

            for digit in range(10):
                if (digit != 0 or current_char not in non_zero_chars) and can_assign(current_char, digit):
                    assign(current_char, digit)
                    if backtrack(index + 1, col, sum_col + digit):
                        return True
                    unassign(current_char, digit)
            return False

        return backtrack(0, 0, 0)