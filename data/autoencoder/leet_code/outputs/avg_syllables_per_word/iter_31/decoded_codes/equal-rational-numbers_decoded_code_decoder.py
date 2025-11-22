from typing import List

class Solution:
    ratios: List[float] = [
        1.0,
        1.0 / 9,
        1.0 / 99,
        1.0 / 999,
        1.0 / 9999,
    ]

    def isRationalEqual(self, s: str, t: str) -> bool:
        def valueOf(s: str) -> float:
            left_paren_index = s.find('(')
            if left_paren_index == -1:
                return float(s)

            right_paren_index = s.find(')')
            dot_index = s.find('.')

            integer_and_non_repeating = float(s[:left_paren_index])
            non_repeating_len = left_paren_index - dot_index - 1

            repeating_str = s[left_paren_index+1:right_paren_index]
            repeating = int(repeating_str) if repeating_str else 0
            repeating_len = right_paren_index - left_paren_index - 1

            return integer_and_non_repeating + repeating * (10 ** -non_repeating_len) * self.ratios[repeating_len]

        return abs(valueOf(s) - valueOf(t)) < 1e-9