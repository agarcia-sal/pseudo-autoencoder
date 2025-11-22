class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = self.build_dictionary(order)
        sorted_characters = self.sort_characters(s, d)
        result_string = self.join_characters(sorted_characters)
        return result_string

    def build_dictionary(self, order: str) -> dict:
        d = {}
        index = 0
        for c in order:
            d[c] = index
            index += 1
        return d

    def sort_characters(self, s: str, d: dict) -> list:
        character_list = list(s)
        character_list.sort(key=lambda c: d.get(c, 0))
        return character_list

    def join_characters(self, character_list: list) -> str:
        result = ''
        for c in character_list:
            result += c
        return result