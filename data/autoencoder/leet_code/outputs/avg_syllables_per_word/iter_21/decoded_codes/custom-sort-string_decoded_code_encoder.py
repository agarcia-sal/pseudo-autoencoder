class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = self.create_custom_order_dictionary(order)
        sorted_characters = self.sort_string_based_on_custom_order(s, d)
        result_string = self.join_characters_into_string(sorted_characters)
        return result_string

    def create_custom_order_dictionary(self, order: str) -> dict:
        dictionary = {}
        index = 0
        for character in order:
            dictionary[character] = index
            index += 1
        return dictionary

    def sort_string_based_on_custom_order(self, s: str, d: dict) -> list:
        list_of_characters = list(s)
        # Characters not in d get a large sort index so they come after ordered chars
        list_of_characters.sort(key=lambda c: d[c] if c in d else len(d) + ord(c))
        return list_of_characters

    def join_characters_into_string(self, character_list: list) -> str:
        result = ""
        for character in character_list:
            result += character
        return result