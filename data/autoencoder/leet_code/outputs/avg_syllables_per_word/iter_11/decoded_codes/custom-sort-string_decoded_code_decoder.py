class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        for i, c in enumerate(order):
            d[c] = i
        sorted_list = sorted(s, key=lambda x: d.get(x, 0))
        result_string = ''.join(sorted_list)
        return result_string