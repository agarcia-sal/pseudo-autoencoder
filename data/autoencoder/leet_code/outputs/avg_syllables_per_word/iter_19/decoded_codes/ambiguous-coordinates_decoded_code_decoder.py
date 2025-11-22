from itertools import product

class Solution:
    def ambiguousCoordinates(self, s):
        def make(frag):
            n = len(frag)
            res = []
            # Generate all valid ways to insert a decimal point
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]

                # Check left part validity: no leading zeros unless left == "0"
                if (left[0] != '0' or left == '0'):
                    # Check right part validity: no trailing zeros if right is non-empty
                    if not right or right[-1] != '0':
                        if right:
                            res.append(left + '.' + right)
                        else:
                            res.append(left)
            return res

        s = s[1:-1]
        result = []
        for i in range(1, len(s)):
            for a, b in product(make(s[:i]), make(s[i:])):
                result.append(f'({a}, {b})')
        return result