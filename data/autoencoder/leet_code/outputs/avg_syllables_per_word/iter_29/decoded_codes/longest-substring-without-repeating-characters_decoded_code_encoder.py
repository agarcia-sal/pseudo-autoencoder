class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapping_of_characters_to_indexes = {}
        maximum_length = 0
        start_position = 0

        for end_position, char in enumerate(s):
            if char in mapping_of_characters_to_indexes and mapping_of_characters_to_indexes[char] >= start_position:
                start_position = mapping_of_characters_to_indexes[char] + 1
            mapping_of_characters_to_indexes[char] = end_position
            maximum_length = max(maximum_length, end_position - start_position + 1)

        return maximum_length