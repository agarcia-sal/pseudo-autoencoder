from typing import List

class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
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

        max_len = max(max(len(w) for w in words), len(result))

        def backtrack(index, col, sum_col):
            if col == max_len:
                return sum_col == 0

            if index == len(words):
                if col < len(result):
                    c = result[len(result) - 1 - col]
                    d = sum_col % 10
                    if c in char_to_digit:
                        if char_to_digit[c] == d:
                            return backtrack(0, col + 1, sum_col // 10)
                        else:
                            return False
                    else:
                        if d == 0 and c in non_zero_chars:
                            return False
                        if can_assign(c, d):
                            assign(c, d)
                            if backtrack(0, col + 1, sum_col // 10):
                                return True
                            unassign(c, d)
                        return False
                else:
                    return sum_col == 0

            w = words[index]
            if col >= len(w):
                return backtrack(index + 1, col, sum_col)

            c = w[len(w) - 1 - col]
            if c in char_to_digit:
                return backtrack(index + 1, col, sum_col + char_to_digit[c])

            for d in range(10):
                if d == 0 and c in non_zero_chars:
                    continue
                if can_assign(c, d):
                    assign(c, d)
                    if backtrack(index + 1, col, sum_col + d):
                        return True
                    unassign(c, d)
            return False

        return backtrack(0, 0, 0)