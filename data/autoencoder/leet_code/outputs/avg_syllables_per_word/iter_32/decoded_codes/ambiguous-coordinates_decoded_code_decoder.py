from typing import List
from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str):
            n = len(frag)
            # Generate all valid string numbers from frag
            # that can represent a coordinate part, 
            # with or without decimal point.
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Conditions:
                # left cannot have leading zeros unless it is '0'
                # right cannot have trailing zeros if it exists (for the fractional part)
                if (left == '0' or left[0] != '0') and (right == '' or right[-1] != '0'):
                    yield left + ('.' + right if right else '')

        s = s[1:-1]  # remove the outer parentheses
        res = []
        for i in range(1, len(s)):
            left_frag = s[:i]
            right_frag = s[i:]
            for a, b in product(make(left_frag), make(right_frag)):
                res.append(f"({a}, {b})")
        return res