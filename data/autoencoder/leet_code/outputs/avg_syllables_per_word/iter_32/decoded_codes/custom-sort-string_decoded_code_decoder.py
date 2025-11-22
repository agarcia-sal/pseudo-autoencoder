from typing import Dict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d: Dict[str, int] = {}
        for i, c in enumerate(order):
            d[c] = i
        # Characters not in 'order' get sorting key 0, same as order[0]'s key
        sorted_list = sorted(s, key=lambda c: d.get(c, 0))
        result = ''.join(sorted_list)
        return result