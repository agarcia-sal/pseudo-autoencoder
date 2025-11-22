class Solution:
    def isRationalEqual(self, s: str, t: str) -> bool:
        ratios = [1, 1/9, 1/99, 1/999, 1/9999]

        def valueOf(s: str) -> float:
            pos_lparen = s.find('(')
            if pos_lparen == -1:
                return float(s)

            pos_rparen = s.find(')')
            pos_dot = s.find('.')

            integer_and_non_repeating = float(s[:pos_lparen])
            length_non_repeating = pos_lparen - pos_dot - 1

            repeating_part = int(s[pos_lparen + 1:pos_rparen])
            length_repeating = pos_rparen - pos_lparen - 1

            value = integer_and_non_repeating + repeating_part * 10**(-length_non_repeating) * ratios[length_repeating]
            return value

        diff = abs(valueOf(s) - valueOf(t))
        return diff < 1e-9