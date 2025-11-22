from typing import List
from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str) -> List[str]:
            n = len(frag)
            res = []
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Check leading zero conditions:
                # left cannot start with '0' unless it is exactly '0'
                # right cannot end with '0' if it is not empty (to avoid trailing zero after decimal)
                if (left == "0" or left[0] != '0') and (not right or right[-1] != '0'):
                    # Assemble number with decimal point if right is not empty
                    res.append(left + ('.' + right if right else ''))
            return res

        s = s[1:-1]
        result = []
        n = len(s)
        for i in range(1, n):
            left_candidates = make(s[:i])
            right_candidates = make(s[i:])
            for a, b in product(left_candidates, right_candidates):
                result.append(f"({a}, {b})")
        return result