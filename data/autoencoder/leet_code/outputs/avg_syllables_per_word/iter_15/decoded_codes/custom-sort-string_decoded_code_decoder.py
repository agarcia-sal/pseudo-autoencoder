from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {c: i for i, c in enumerate(order)}
        # Characters not in order get priority 0, so they appear before those in order
        sorted_chars = sorted(s, key=lambda x: d.get(x, 0))
        return ''.join(sorted_chars)