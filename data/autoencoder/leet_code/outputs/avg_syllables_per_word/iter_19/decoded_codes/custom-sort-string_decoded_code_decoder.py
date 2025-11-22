class Solution:
    def customSortString(self, order, s):
        d = {c: i for i, c in enumerate(order)}
        return ''.join(sorted(s, key=lambda x: d.get(x, 0)))