class Solution:
    def customSortString(self, order, s):
        d = {}
        i = 0
        for character in order:
            d[character] = i
            i += 1
        list_of_characters = sorted(s, key=lambda c: d[c] if c in d else 0)
        result_string = ''.join(list_of_characters)
        return result_string