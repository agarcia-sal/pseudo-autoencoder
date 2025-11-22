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
            max_len = max(max(len(w) for w in words), len(result))
            if col >= max_len:
                return sum_col == 0

            if index == len(words):
                if col < len(result):
                    ch = result[len(result) - 1 - col]
                    digit = sum_col % 10
                    if ch in char_to_digit:
                        if char_to_digit[ch] == digit:
                            return backtrack(0, col + 1, sum_col // 10)
                        else:
                            return False
                    else:
                        if can_assign(ch, digit) and (digit != 0 or ch not in non_zero_chars):
                            assign(ch, digit)
                            if backtrack(0, col + 1, sum_col // 10):
                                return True
                            unassign(ch, digit)
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