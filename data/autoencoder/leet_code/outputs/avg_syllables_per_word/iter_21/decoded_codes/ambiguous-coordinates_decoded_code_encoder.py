from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str) -> list[str]:
            n = len(frag)
            result = []
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # Left part should not start with '0' unless it is exactly '0'
                if (left == "0" or not left.startswith("0")) and (right == "" or not right.endswith("0")):
                    if right:
                        result.append(left + "." + right)
                    else:
                        result.append(left)
            return result

        s = s[1:-1]
        result = []
        for i in range(1, len(s)):
            left_frag = s[:i]
            right_frag = s[i:]
            for a, b in product(make(left_frag), make(right_frag)):
                result.append(f"({a}, {b})")
        return result