class Solution:
    def customSortString(self, order_string: str, s_string: str) -> str:
        character_order_dictionary = self.buildCharacterOrderDictionary(order_string)
        sorted_character_list = self.sortStringWithCustomOrder(s_string, character_order_dictionary)
        result_string = self.joinCharacters(sorted_character_list)
        return result_string

    def buildCharacterOrderDictionary(self, order_string: str) -> dict:
        order_dictionary = {}
        for index in range(len(order_string)):
            character_at_position = order_string[index]
            value_at_character = index
            order_dictionary[character_at_position] = value_at_character
        return order_dictionary

    def sortStringWithCustomOrder(self, s_string: str, order_dictionary: dict) -> list:
        list_of_characters = self.convertStringToList(s_string)
        sorted_list = self.sortCharactersByOrderDictionary(list_of_characters, order_dictionary)
        return sorted_list

    def convertStringToList(self, s_string: str) -> list:
        # Simply convert string to list of characters
        return list(s_string)

    def sortCharactersByOrderDictionary(self, list_of_characters: list, order_dictionary: dict) -> list:
        # Characters not in order_dictionary get a large order index so they come last, preserving their relative order by stable sort
        max_order = len(order_dictionary)
        # Key function looks up character order; if not found returns max_order
        return sorted(list_of_characters, key=lambda ch: order_dictionary.get(ch, max_order))

    def joinCharacters(self, list_of_characters: list) -> str:
        # Join characters into a single string
        return ''.join(list_of_characters)