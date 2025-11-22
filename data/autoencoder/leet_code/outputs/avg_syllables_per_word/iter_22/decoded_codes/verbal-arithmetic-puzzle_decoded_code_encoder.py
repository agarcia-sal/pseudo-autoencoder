class Solution:
    def isSolvable(self, words, result):
        unique_chars = set(char for word in words for char in word) | set(result)
        if len(unique_chars) > 10:
            return False

        non_zero_chars = set(word[0] for word in words if len(word) > 1)
        if len(result) > 1:
            non_zero_chars.add(result[0])

        char_to_digit = {}
        digit_to_char = {}

        def can_assign(character, digit):
            return (character not in char_to_digit) and (digit not in digit_to_char or digit_to_char[digit] == character)

        def assign(character, digit):
            char_to_digit[character] = digit
            digit_to_char[digit] = character

        def unassign(character, digit):
            char_to_digit.pop(character)
            digit_to_char.pop(digit)

        def word_value(word):
            total_sum = 0
            for i, ch in enumerate(reversed(word)):
                total_sum += char_to_digit[ch] * (10 ** i)
            return total_sum

        def backtrack(index, col, sum_col):
            max_len = max(len(w) for w in words)
            if col >= max_len and col >= len(result):
                return sum_col == 0

            if index == len(words):
                if col < len(result):
                    digit_char = result[len(result) - 1 - col]
                    remainder = sum_col % 10
                    if digit_char in char_to_digit:
                        if char_to_digit[digit_char] == remainder:
                            return backtrack(0, col + 1, sum_col // 10)
                        else:
                            return False
                    else:
                        if can_assign(digit_char, remainder) and (remainder != 0 or digit_char not in non_zero_chars):
                            assign(digit_char, remainder)
                            if backtrack(0, col + 1, sum_col // 10):
                                return True
                            unassign(digit_char, remainder)
                    return False
                else:
                    return sum_col == 0

            word = words[index]
            if col >= len(word):
                return backtrack(index + 1, col, sum_col)

            ch = word[len(word) - 1 - col]
            if ch in char_to_digit:
                return backtrack(index + 1, col, sum_col + char_to_digit[ch])

            for digit in range(10):
                if can_assign(ch, digit) and (digit != 0 or ch not in non_zero_chars):
                    assign(ch, digit)
                    if backtrack(index + 1, col, sum_col + digit):
                        return True
                    unassign(ch, digit)

            return False

        return backtrack(0, 0, 0)