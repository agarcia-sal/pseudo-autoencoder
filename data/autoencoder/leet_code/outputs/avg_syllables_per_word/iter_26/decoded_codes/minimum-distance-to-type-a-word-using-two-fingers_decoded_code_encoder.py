from functools import lru_cache

class Solution:
    def minimumDistance(self, word: str) -> int:
        def distance(character_one, character_two):
            if character_one is None:
                return 0
            pos_one_row = (ord(character_one) - ord('A')) // 6
            pos_one_col = (ord(character_one) - ord('A')) % 6
            pos_two_row = (ord(character_two) - ord('A')) // 6
            pos_two_col = (ord(character_two) - ord('A')) % 6
            return abs(pos_one_row - pos_two_row) + abs(pos_one_col - pos_two_col)

        @lru_cache(maxsize=None)
        def dp(index, finger_one_character, finger_two_character):
            if index == len(word):
                return 0
            current_character = word[index]
            distance_one = distance(finger_one_character, current_character) + dp(index + 1, current_character, finger_two_character)
            distance_two = distance(finger_two_character, current_character) + dp(index + 1, finger_one_character, current_character)
            return min(distance_one, distance_two)

        return dp(0, None, None)