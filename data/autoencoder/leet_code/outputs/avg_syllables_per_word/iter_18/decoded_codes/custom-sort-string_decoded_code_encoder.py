class Solution:
    def customSortString(self, order: str, s: str) -> str:
        character_index_mapping = self.create_character_index_mapping(order)
        sorted_characters = self.sort_characters_by_custom_order(s, character_index_mapping)
        result_string = self.join_characters(sorted_characters)
        return result_string

    def create_character_index_mapping(self, order: str) -> dict:
        character_index_mapping = {}
        current_index = 0
        for character in order:
            character_index_mapping[character] = current_index
            current_index += 1
        return character_index_mapping

    def sort_characters_by_custom_order(self, s: str, character_index_mapping: dict) -> list:
        character_list = list(s)
        character_list.sort(key=lambda c: character_index_mapping[c] if c in character_index_mapping else len(character_index_mapping))
        return character_list

    def join_characters(self, list_of_characters: list) -> str:
        concatenated_string = ''
        for character in list_of_characters:
            concatenated_string += character
        return concatenated_string