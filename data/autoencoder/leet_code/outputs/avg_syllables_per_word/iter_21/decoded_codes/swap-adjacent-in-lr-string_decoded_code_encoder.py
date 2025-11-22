class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        start_filtered = self.list_of_character_and_index_pairs_excluding_character(start, 'X')
        end_filtered = self.list_of_character_and_index_pairs_excluding_character(end, 'X')

        if len(start_filtered) != len(end_filtered):
            return False

        for (char_one, index_one), (char_two, index_two) in zip(start_filtered, end_filtered):
            if char_one != char_two:
                return False
            if char_one == 'L' and index_one < index_two:
                return False
            if char_one == 'R' and index_one > index_two:
                return False

        return True

    def list_of_character_and_index_pairs_excluding_character(self, input_string: str, character_to_exclude: str):
        result_list = []
        for index, char in enumerate(input_string):
            if char != character_to_exclude:
                result_list.append((char, index))
        return result_list