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

        def can_assign(c, d):
            return c not in char_to_digit and (d not in digit_to_char or digit_to_char[d] == c)

        def assign(c, d):
            char_to_digit[c] = d
            digit_to_char[d] = c

        def unassign(c, d):
            del char_to_digit[c]
            del digit_to_char[d]

        def backtrack(index, column, carry):
            max_len = max(map(len, words + [result]))
            if column >= max_len:
                return carry == 0

            if index == len(words):
                if column < len(result):
                    r_char = result[len(result) - 1 - column]
                    d = carry % 10
                    if r_char in char_to_digit:
                        if char_to_digit[r_char] == d:
                            return backtrack(0, column + 1, carry // 10)
                        return False
                    if can_assign(r_char, d) and (d != 0 or r_char not in non_zero_chars):
                        assign(r_char, d)
                        if backtrack(0, column + 1, carry // 10):
                            return True
                        unassign(r_char, d)
                else:
                    return carry == 0
                return False

            w = words[index]
            if column >= len(w):
                return backtrack(index + 1, column, carry)

            c = w[len(w) - 1 - column]
            if c in char_to_digit:
                return backtrack(index + 1, column, carry + char_to_digit[c])

            for d in range(10):
                if can_assign(c, d) and (d != 0 or c not in non_zero_chars):
                    assign(c, d)
                    if backtrack(index + 1, column, carry + d):
                        return True
                    unassign(c, d)

            return False

        return backtrack(0, 0, 0)