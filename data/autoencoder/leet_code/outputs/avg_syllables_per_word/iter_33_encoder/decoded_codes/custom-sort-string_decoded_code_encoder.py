class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {c: i for i, c in enumerate(order)}
        sorted_list = sorted(s, key=lambda x: d.get(x, 0))
        result_string = ''.join(sorted_list)
        return result_string