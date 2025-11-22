class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str) -> list[str]:
            n = len(frag)
            res = []
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                if (left == "0" or not left.startswith("0")) and (right == "" or not right.endswith("0")):
                    if d != n:
                        res.append(left + "." + right)
                    else:
                        res.append(left)
            return res

        s = s[1:-1]
        result = []
        for i in range(1, len(s)):
            for a in make(s[:i]):
                for b in make(s[i:]):
                    result.append(f"({a}, {b})")
        return result