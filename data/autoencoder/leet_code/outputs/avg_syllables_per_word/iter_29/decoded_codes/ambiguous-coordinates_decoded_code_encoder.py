from typing import List
from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str):
            n = len(frag)
            for i in range(1, n + 1):
                left_part = frag[:i]
                right_part = frag[i:]
                # Check conditions:
                # left_part cannot start with '0' unless it is '0'
                # right_part cannot end with '0' (to avoid trailing zeros after dot)
                if (left_part == '0' or left_part[0] != '0') and (not right_part or right_part[-1] != '0'):
                    yield left_part + ('.' if right_part else '') + right_part

        s = s[1:-1]  # remove the outer parentheses
        res = []
        for i in range(1, len(s)):
            left_frag = s[:i]
            right_frag = s[i:]
            for left_element, right_element in product(make(left_frag), make(right_frag)):
                res.append(f"({left_element}, {right_element})")
        return res