from typing import List, Dict, Set


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        unique_chars: Set[str] = set()
        for w in words:
            unique_chars.update(w)
        unique_chars.update(result)
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
            if char in char_to_digit:
                return False
            if digit not in digit_to_char or digit_to_char[digit] == char:
                return True
            return False

        def assign(char: str, digit: int) -> None:
            char_to_digit[char] = digit
            digit_to_char[digit] = char

        def unassign(char: str, digit: int) -> None:
            char_to_digit.pop(char, None)
            digit_to_char.pop(digit, None)

        max_len = max(max(len(w) for w in words), len(result))

        def backtrack(index: int, col: int, sum_col: int) -> bool:
            if col >= max_len and col >= len(result):
                return sum_col == 0

            if index == len(words):
                if col < len(result):
                    digit_char = result[len(result) - 1 - col]
                    mod_digit = sum_col % 10
                    if digit_char in char_to_digit:
                        if char_to_digit[digit_char] == mod_digit:
                            return backtrack(0, col + 1, sum_col // 10)
                        else:
                            return False
                    else:
                        if can_assign(digit_char, mod_digit) and (mod_digit != 0 or digit_char not in non_zero_chars):
                            assign(digit_char, mod_digit)
                            if backtrack(0, col + 1, sum_col // 10):
                                return True
                            unassign(digit_char, mod_digit)
                        return False
                else:
                    return sum_col == 0

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