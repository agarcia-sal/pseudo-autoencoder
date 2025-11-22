from typing import List
from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str):
            n = len(frag)
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Check left part validity: no leading zero unless single '0'
                if (left[0] != '0' or left == '0') and (not right or right[-1] != '0'):
                    if right:
                        yield left + '.' + right
                    else:
                        yield left

        s = s[1:-1]  # strip the parentheses
        result = []
        for i in range(1, len(s)):
            for a, b in product(make(s[:i]), make(s[i:])):
                result.append(f"({a}, {b})")
        return result