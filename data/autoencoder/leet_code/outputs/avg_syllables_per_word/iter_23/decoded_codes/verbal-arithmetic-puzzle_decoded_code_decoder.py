from typing import List, Dict, Set

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        unique_chars: Set[str] = set()
        for w in words:
            unique_chars.update(w)
        unique_chars.update(result)
        if len(unique_chars) > 10:
            return False

        # Collect characters that cannot be assigned zero because they're leading chars
        non_zero_chars: Set[str] = set()
        for w in words:
            if len(w) > 1:
                non_zero_chars.add(w[0])
        if len(result) > 1:
            non_zero_chars.add(result[0])

        char_to_digit: Dict[str, int] = {}
        digit_to_char: Dict[int, str] = {}

        def can_assign(char: str, digit: int) -> bool:
            return (char not in char_to_digit) and (digit not in digit_to_char or digit_to_char[digit] == char)

        def assign(char: str, digit: int):
            char_to_digit[char] = digit
            digit_to_char[digit] = char

        def unassign(char: str, digit: int):
            char_to_digit.pop(char)
            digit_to_char.pop(digit)

        def word_value(word: str) -> int:
            total_value = 0
            length = len(word)
            for index, char in enumerate(reversed(word)):
                total_value += char_to_digit[char] * (10 ** index)
            return total_value

        # Precompute max length for columns
        max_length = max(max(len(w) for w in words), len(result))

        def backtrack(index: int, col: int, sum_col: int) -> bool:
            if col >= max_length:
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
                        d = sum_col % 10
                        if can_assign(digit_char, d) and (d != 0 or digit_char not in non_zero_chars):
                            assign(digit_char, d)
                            if backtrack(0, col + 1, sum_col // 10):
                                return True
                            unassign(digit_char, d)
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