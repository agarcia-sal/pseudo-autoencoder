from itertools import product

class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str) -> list[str]:
            n = len(frag)
            res = []
            for d in range(1, n + 1):
                left, right = frag[:d], frag[d:]
                # Check conditions for valid number formatting
                # left should not start with '0' unless it is '0' itself
                # right should not end with '0' if it is not empty
                if (left == "0" or not left.startswith("0")) and (not right.endswith("0")):
                    # Add decimal if right part exists, else just left
                    if right:
                        res.append(left + "." + right)
                    else:
                        res.append(left)
            return res

        s = s[1:-1]  # strip outer parentheses
        n = len(s)
        ans = []
        for i in range(1, n):
            left_parts = make(s[:i])
            right_parts = make(s[i:])
            for a, b in product(left_parts, right_parts):
                ans.append(f"({a}, {b})")
        return ans