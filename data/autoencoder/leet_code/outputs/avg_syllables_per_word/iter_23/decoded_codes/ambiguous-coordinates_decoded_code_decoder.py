from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str):
            n = len(frag)
            for d in range(1, n+1):
                left = frag[:d]
                right = frag[d:]
                # conditions:
                # left must not start with '0' unless it's exactly "0"
                # right must not end with '0' (if it exists)
                if (left[0] != '0' or left == "0") and (right == "" or right[-1] != '0'):
                    yield left + ('.' + right if d != n else '')
        s = s[1:-1]
        res = []
        for i in range(1, len(s)):
            for a, b in product(make(s[:i]), make(s[i:])):
                res.append(f"({a}, {b})")
        return res