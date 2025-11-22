from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str):
            n = len(frag)
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Conditions:
                # left cannot start with '0' unless it is '0' itself,
                # and right cannot end with '0' to be valid decimal part.
                if (left[0] != '0' or left == '0') and (not right or right[-1] != '0'):
                    yield left + ('.' if d != n else '') + right

        s = s[1:-1]
        res = []
        for i in range(1, len(s)):
            # Make all possible left parts
            left_parts = list(make(s[:i]))
            # Make all possible right parts
            right_parts = list(make(s[i:]))
            for a, b in product(left_parts, right_parts):
                res.append(f"({a}, {b})")
        return res