class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d = self.create_dictionary_for_custom_order(order)
        sorted_characters = self.sort_string_s_by_custom_order(s, d)
        result_string = self.concatenate_characters(sorted_characters)
        return result_string

    def create_dictionary_for_custom_order(self, order: str) -> dict:
        d = {}
        index = 0
        for character in order:
            d[character] = index
            index += 1
        return d

    def sort_string_s_by_custom_order(self, s: str, d: dict) -> list:
        list_of_characters = list(s)
        sorted_list = []

        while list_of_characters:
            # Find character with the lowest order value (characters not in d get order 0)
            # According to original pseudocode, characters not in d get 0, 
            # but that would treat unknown chars as highest priority - 
            # it's ambiguous but we preserve that logic exactly.
            # To comply exactly, we define order_value = d.get(char, 0)

            # Find minimal order value among remaining characters
            min_order_value = min(d.get(c, 0) for c in list_of_characters)
            # Collect all characters with this minimum order value in their original order
            to_append = [c for c in list_of_characters if d.get(c, 0) == min_order_value]
            # Append them to sorted_list in the order they appear
            sorted_list.extend(to_append)
            # Remove these characters from list_of_characters in the same order
            new_list = []
            idx = 0
            for c in list_of_characters:
                if d.get(c, 0) == min_order_value:
                    # skip
                    continue
                new_list.append(c)
            list_of_characters = new_list

        return sorted_list

    def concatenate_characters(self, characters_list: list) -> str:
        result_string = ""
        for character in characters_list:
            result_string += character
        return result_string