class Solution:
    def customSortString(self, order, s):
        d = {}
        for i in range(len(order)):
            c = order[i]
            d[c] = i
        sorted_list = sorted(s, key=lambda x: d.get(x, 0))
        result = ''.join(sorted_list)
        return result