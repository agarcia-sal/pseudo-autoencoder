from typing import List
from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str):
            n = len(frag)
            # Generate all valid decimal representations from frag
            for d in range(1, n + 1):
                left_part = frag[:d]
                right_part = frag[d:]
                # Conditions:
                # left_part can't have leading zeros unless it's '0' itself
                # right_part can't have trailing zeros if not empty
                if (left_part[0] != '0' or left_part == "0") and (not right_part or right_part[-1] != '0'):
                    if d != n:
                        yield left_part + '.' + right_part
                    else:
                        yield left_part

        s = s[1:-1]  # strip parentheses
        res = []
        for i in range(1, len(s)):
            for a, b in product(make(s[:i]), make(s[i:])):
                res.append(f"({a}, {b})")
        return res