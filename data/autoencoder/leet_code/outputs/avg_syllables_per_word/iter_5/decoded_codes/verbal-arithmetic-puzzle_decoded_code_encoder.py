class Solution:
    def isSolvable(self, words, result):
        unique_chars = set("".join(words) + result)
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

        max_len = max(max(map(len, words)), len(result))

        def backtrack(i, col, sum_col):
            if col >= max_len:
                return sum_col == 0

            if i == len(words):
                if col < len(result):
                    c = result[len(result) - 1 - col]
                    d = sum_col % 10
                    if c in char_to_digit:
                        if char_to_digit[c] == d:
                            return backtrack(0, col + 1, sum_col // 10)
                        return False
                    if can_assign(c, d) and (d != 0 or c not in non_zero_chars):
                        assign(c, d)
                        if backtrack(0, col + 1, sum_col // 10):
                            return True
                        unassign(c, d)
                    return False
                else:
                    return sum_col == 0

            word = words[i]
            if col >= len(word):
                return backtrack(i + 1, col, sum_col)

            c = word[len(word) - 1 - col]
            if c in char_to_digit:
                return backtrack(i + 1, col, sum_col + char_to_digit[c])

            for d in range(10):
                if can_assign(c, d) and (d != 0 or c not in non_zero_chars):
                    assign(c, d)
                    if backtrack(i + 1, col, sum_col + d):
                        return True
                    unassign(c, d)
            return False

        return backtrack(0, 0, 0)