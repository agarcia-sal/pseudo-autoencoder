from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str):
            n = len(frag)
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Check validity: left can't have leading zeros unless it is '0'
                if (left[0] != '0' or left == "0") and (not right or right[-1] != '0'):
                    yield left + ('.' if d != n else '') + right

        s = s[1:-1]  # strip parentheses
        return [
            f"({a}, {b})"
            for i in range(1, len(s))
            for a, b in product(make(s[:i]), make(s[i:]))
        ]