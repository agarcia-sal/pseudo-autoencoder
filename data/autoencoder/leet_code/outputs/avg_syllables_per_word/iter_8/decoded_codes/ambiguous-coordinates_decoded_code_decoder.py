from itertools import product

class Solution:
    def ambiguousCoordinates(self, s):
        def make(frag):
            n = len(frag)
            for d in range(1, n + 1):
                left = frag[:d]
                right = frag[d:]
                if (not (left.startswith('0') and left != '0')) and (right == '' or not right.endswith('0')):
                    yield left + ('.' if d != n else '') + right

        s = s[1:-1]
        result = []
        for i in range(1, len(s)):
            for a, b in product(make(s[:i]), make(s[i:])):
                result.append(f'({a}, {b})')
        return result