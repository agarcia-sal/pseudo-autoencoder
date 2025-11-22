from typing import List

class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        def make(frag: str) -> List[str]:
            n = len(frag)
            res = []
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # left should not start with '0' unless it is exactly '0'
                if (left[0] != '0' or left == "0"):
                    # right should not end with '0' if it's not empty
                    if right == "" or right[-1] != '0':
                        if d != n:
                            res.append(left + "." + right)
                        else:
                            res.append(left)
            return res

        s = s[1:-1]  # remove enclosing parentheses
        result_list = []
        for i in range(1, len(s)):
            for a in make(s[:i]):
                for b in make(s[i:]):
                    result_list.append(f"({a}, {b})")
        return result_list