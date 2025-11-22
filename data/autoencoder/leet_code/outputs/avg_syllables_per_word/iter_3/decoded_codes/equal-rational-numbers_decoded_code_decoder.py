class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios = [1, 1/9, 1/99, 1/999, 1/9999]

        def valueOf(x: str) -> float:
            if '(' not in x:
                return float(x)
            left = x.index('(')
            right = x.index(')')
            dot = x.index('.')
            integer_and_nonrepeating = float(x[:left])
            non_repeating_length = left - dot - 1
            repeating = int(x[left+1:right])
            repeating_length = right - left - 1
            return integer_and_nonrepeating + repeating * (0.1 ** non_repeating_length) * ratios[repeating_length]

        return abs(valueOf(s) - valueOf(t)) < 1e-9