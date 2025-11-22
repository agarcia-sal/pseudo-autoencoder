class Solution:
    def isSolvable(self, words, result):
        unique_characters = set(''.join(words) + result)
        if len(unique_characters) > 10:
            return False

        non_zero_characters = set()
        for w in words:
            if len(w) > 1:
                non_zero_characters.add(w[0])
        if len(result) > 1:
            non_zero_characters.add(result[0])
        else:
            non_zero_characters.add('')

        char_to_digit = {}
        digit_to_char = {}

        def can_assign(character, digit):
            return (
                character not in char_to_digit and
                (digit not in digit_to_char or digit_to_char[digit] == character)
            )

        def assign(character, digit):
            char_to_digit[character] = digit
            digit_to_char[digit] = character

        def unassign(character, digit):
            del char_to_digit[character]
            del digit_to_char[digit]

        def backtrack(index, column, sum_column):
            max_len = max((len(w) for w in words), default=0)
            if column >= max_len and column >= len(result):
                return sum_column == 0

            if index == len(words):
                if column < len(result):
                    character = result[len(result) - 1 - column]
                    digit = sum_column % 10
                    if character in char_to_digit:
                        if char_to_digit[character] == digit:
                            return backtrack(0, column + 1, sum_column // 10)
                        else:
                            return False
                    else:
                        if can_assign(character, digit) and (digit != 0 or character not in non_zero_characters):
                            assign(character, digit)
                            if backtrack(0, column + 1, sum_column // 10):
                                return True
                            unassign(character, digit)
                        return False
                else:
                    return sum_column == 0

            word = words[index]
            if column >= len(word):
                return backtrack(index + 1, column, sum_column)

            character = word[len(word) - 1 - column]
            if character in char_to_digit:
                return backtrack(index + 1, column, sum_column + char_to_digit[character])

            for digit in range(10):
                if can_assign(character, digit) and (digit != 0 or character not in non_zero_characters):
                    assign(character, digit)
                    if backtrack(index + 1, column, sum_column + digit):
                        return True
                    unassign(character, digit)
            return False

        return backtrack(0, 0, 0)