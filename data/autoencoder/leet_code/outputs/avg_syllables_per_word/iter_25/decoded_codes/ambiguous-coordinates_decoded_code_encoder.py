from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str):
            n = len(frag)
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # left is valid if it is '0' or does not start with '0'
                # right is valid if it is empty or does not end with '0'
                if (left == "0" or left[0] != "0") and (right == "" or right[-1] != "0"):
                    yield left + ('.' if d != n else '') + right

        s = s[1:-1]  # remove the outer parentheses
        result = []
        for i in range(1, len(s)):
            for a, b in product(make(s[:i]), make(s[i:])):
                result.append(f"({a}, {b})")
        return result