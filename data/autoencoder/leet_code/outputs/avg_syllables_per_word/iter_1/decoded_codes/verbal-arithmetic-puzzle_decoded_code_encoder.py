def is_solvable(words, result):
    unique_chars = set(''.join(words) + result)
    if len(unique_chars) > 10:
        return False

    non_zero = {w[0] for w in words if len(w) > 1}
    if len(result) > 1:
        non_zero.add(result[0])

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

    def backtrack(i, col, carry):
        max_len = max(len(w) for w in words)
        if col >= max_len and col >= len(result):
            return carry == 0

        if i == len(words):
            if col < len(result):
                c = result[len(result) - 1 - col]
                digit = carry % 10
                if c in char_to_digit:
                    if char_to_digit[c] != digit:
                        return False
                    return backtrack(0, col + 1, carry // 10)
                if can_assign(c, digit) and (digit != 0 or c not in non_zero):
                    assign(c, digit)
                    if backtrack(0, col + 1, carry // 10):
                        return True
                    unassign(c, digit)
                return False
            else:
                return carry == 0

        w = words[i]
        if col >= len(w):
            return backtrack(i + 1, col, carry)
        c = w[len(w) - 1 - col]
        if c in char_to_digit:
            return backtrack(i + 1, col, carry + char_to_digit[c])

        for d in range(10):
            if can_assign(c, d) and (d != 0 or c not in non_zero):
                assign(c, d)
                if backtrack(i + 1, col, carry + d):
                    return True
                unassign(c, d)
        return False

    return backtrack(0, 0, 0)