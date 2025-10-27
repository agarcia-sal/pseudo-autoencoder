from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str):
            n = len(frag)
            # Generate valid decimal representations from `frag`
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Check leading zero constraints
                if (left[0] != '0' or left == '0') and (right == '' or right[-1] != '0'):
                    # Insert decimal point if there's a fractional part
                    yield left + ('.' + right if d != n else '')

        s = s[1:-1]

        return [
            f"({a}, {b})"
            for i in range(1, len(s))
            for a, b in product(make(s[:i]), make(s[i:]))
        ]