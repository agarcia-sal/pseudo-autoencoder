class Solution:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def make(frag: str) -> list[str]:
            n = len(frag)
            res = []
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                # left cannot start with '0' unless it is exactly '0'
                # right cannot end with '0' if it is non-empty
                if (left[0] != '0' or left == '0') and (right == '' or right[-1] != '0'):
                    if right == '':
                        res.append(left)
                    else:
                        res.append(left + '.' + right)
            return res

        s = s[1:-1]
        res = []
        for i in range(1, len(s)):
            for a in make(s[:i]):
                for b in make(s[i:]):
                    res.append(f"({a}, {b})")
        return res