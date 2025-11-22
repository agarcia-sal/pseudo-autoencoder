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

        max_len = max(max(map(len, words)), len(result))

        def backtrack(index, col, sum_col):
            if col >= max_len and col >= len(result):
                return sum_col == 0

            if index == len(words):
                if col < len(result):
                    digit_char = result[len(result) - 1 - col]
                    d = sum_col % 10
                    if digit_char in char_to_digit:
                        if char_to_digit[digit_char] == d:
                            return backtrack(0, col + 1, sum_col // 10)
                        return False
                    if can_assign(digit_char, d) and (d != 0 or digit_char not in non_zero_chars):
                        assign(digit_char, d)
                        if backtrack(0, col + 1, sum_col // 10):
                            return True
                        unassign(digit_char, d)
                    return False
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