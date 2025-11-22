from typing import List, Set, Dict

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
            if char in char_to_digit:
                return False
            if digit in digit_to_char and digit_to_char[digit] != char:
                return False
            return True

        def assign(char: str, digit: int) -> None:
            char_to_digit[char] = digit
            digit_to_char[digit] = char

        def unassign(char: str, digit: int) -> None:
            del char_to_digit[char]
            del digit_to_char[digit]

        def word_value(word: str) -> int:
            total_value = 0
            for idx, ch in enumerate(reversed(word)):
                total_value += char_to_digit[ch] * (10 ** idx)
            return total_value

        max_word_length = max((len(w) for w in words), default=0)

        def backtrack(index: int, col: int, sum_col: int) -> bool:
            if col >= max_word_length and col >= len(result):
                return sum_col == 0

            if index == len(words):
                if col < len(result):
                    digit_char = result[len(result) - 1 - col]
                    digit = sum_col % 10

                    if digit_char in char_to_digit:
                        if char_to_digit[digit_char] != digit:
                            return False
                        return backtrack(0, col + 1, sum_col // 10)

                    # When digit_char not assigned yet
                    if (digit == 0 and digit_char in non_zero_chars) or not can_assign(digit_char, digit):
                        return False

                    assign(digit_char, digit)
                    if backtrack(0, col + 1, sum_col // 10):
                        return True
                    unassign(digit_char, digit)
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
                if (digit == 0 and current_char in non_zero_chars) or not can_assign(current_char, digit):
                    continue

                assign(current_char, digit)
                if backtrack(index + 1, col, sum_col + digit):
                    return True
                unassign(current_char, digit)

            return False

        return backtrack(0, 0, 0)