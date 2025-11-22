from collections import Counter
from typing import List

class Solution:
    def maxScoreWords(self, words_list: List[str], letters_list: List[str], score_list: List[int]) -> int:
        def word_score(word_string: str, score_mapping: List[int]) -> int:
            # Calculate the total score of the word based on score_mapping
            return sum(score_mapping[ord(ch) - ord('a')] for ch in word_string)

        def can_form(word_string: str, letter_count_map: Counter) -> bool:
            word_count_map = Counter(word_string)
            for ch, cnt in word_count_map.items():
                if letter_count_map[ch] < cnt:
                    return False
            return True

        def update_letter_count(letter_count_map: Counter, word_string: str, add_indicator: bool = True) -> None:
            delta = 1 if add_indicator else -1
            for ch in word_string:
                letter_count_map[ch] += delta

        def backtrack(index_position: int, current_score_value: int, letter_count_map: Counter) -> int:
            if index_position == len(words_list):
                return current_score_value

            max_score_value = current_score_value
            for i in range(index_position, len(words_list)):
                word = words_list[i]
                if can_form(word, letter_count_map):
                    update_letter_count(letter_count_map, word, add_indicator=False)
                    score = backtrack(i + 1, current_score_value + word_score(word, score_mapping), letter_count_map)
                    max_score_value = max(max_score_value, score)
                    update_letter_count(letter_count_map, word, add_indicator=True)
            return max_score_value

        score_mapping = score_list
        letter_count_map = Counter(letters_list)
        return backtrack(0, 0, letter_count_map)