from typing import Dict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d: Dict[str, int] = {}
        for i, c in enumerate(order):
            d[c] = i
        # Characters not in order have key equal to len(order) to be placed last
        sorted_chars = sorted(s, key=lambda x: d.get(x, len(order)))
        return "".join(sorted_chars)