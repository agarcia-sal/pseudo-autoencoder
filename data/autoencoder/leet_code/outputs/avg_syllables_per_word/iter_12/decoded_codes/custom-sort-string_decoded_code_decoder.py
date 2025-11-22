class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = {}
        for index in range(len(order)):
            char = order[index]
            d[char] = index
        sorted_list = sorted(s, key=lambda x: d[x] if x in d else 0)
        result_string = ''.join(sorted_list)
        return result_string