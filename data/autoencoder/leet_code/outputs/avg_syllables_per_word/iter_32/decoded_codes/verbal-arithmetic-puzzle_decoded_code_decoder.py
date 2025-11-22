from typing import List, Set, Dict

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        # Collect all unique characters from words and result
        unique_chars: Set[str] = set()
        for w in words:
            unique_chars.update(w)
        unique_chars.update(result)

        # If more than 10 unique chars, no solution since digits 0-9 only
        if len(unique_chars) > 10:
            return False

        # Characters that cannot be zero (leading chars of words or result if length >1)
        non_zero_chars: Set[str] = set()
        for w in words:
            if len(w) > 1:
                non_zero_chars.add(w[0])
        if len(result) > 1:
            non_zero_chars.add(result[0])

        char_to_digit: Dict[str, int] = {}
        digit_to_char: Dict[int, str] = {}

        def can_assign(c: str, d: int) -> bool:
            # Can assign if char not assigned AND digit not assigned or assigned to same char
            return (c not in char_to_digit and (d not in digit_to_char or digit_to_char[d] == c))

        def assign(c: str, d: int) -> None:
            char_to_digit[c] = d
            digit_to_char[d] = c

        def unassign(c: str, d: int) -> None:
            del char_to_digit[c]
            del digit_to_char[d]

        def word_value(word: str) -> int:
            total = 0
            for i, ch in enumerate(reversed(word)):
                total += char_to_digit[ch] * (10 ** i)
            return total

        max_len = max(max(len(w) for w in words), len(result))

        def backtrack(index: int, col: int, sum_col: int) -> bool:
            # Base: if all columns processed
            if col >= max_len:
                return sum_col == 0

            if index == len(words):
                # Verify result digit at current column
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
                        return False
                else:
                    return sum_col == 0

            current_word = words[index]
            # If current word too short for this column, move to next word
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