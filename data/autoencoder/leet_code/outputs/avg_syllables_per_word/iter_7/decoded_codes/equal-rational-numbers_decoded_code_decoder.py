from typing import List


class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios: List[float] = [1, 1 / 9, 1 / 99, 1 / 999, 1 / 9999]

        def valueOf(s: str) -> float:
            if '(' not in s:
                return float(s)

            left_paren_index = s.index('(')
            right_paren_index = s.index(')')
            dot_index = s.index('.')

            integer_and_non_repeating = float(s[:left_paren_index])
            non_repeating_length = left_paren_index - dot_index - 1

            repeating = int(s[left_paren_index + 1:right_paren_index])
            repeating_length = right_paren_index - left_paren_index - 1

            return integer_and_non_repeating + repeating * 10 ** (-non_repeating_length) * ratios[repeating_length]

        return abs(valueOf(s) - valueOf(t)) < 1e-9