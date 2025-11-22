from typing import Dict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d: Dict[str, int] = {}
        for i, char in enumerate(order):
            d[char] = i
        # Characters not in `order` get a default sort key bigger than any index in d to preserve relative order after ordered chars
        max_order = len(order)
        sorted_list = sorted(s, key=lambda c: d.get(c, max_order))
        return ''.join(sorted_list)