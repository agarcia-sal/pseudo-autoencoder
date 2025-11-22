class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios = [1 / 9, 1 / 99, 1 / 999, 1 / 9999]

        def valueOf(x: str) -> float:
            left_paren_index = x.find('(')
            if left_paren_index == -1:
                return float(x)

            right_paren_index = x.find(')')
            dot_index = x.find('.')

            integer_and_non_repeating = float(x[:left_paren_index])
            non_repeating_length = left_paren_index - dot_index - 1

            repeating = int(x[left_paren_index + 1:right_paren_index])
            repeating_length = right_paren_index - left_paren_index - 1

            return integer_and_non_repeating + repeating * (10 ** (-non_repeating_length)) * ratios[repeating_length - 1]

        return abs(valueOf(s) - valueOf(t)) < 1e-9