from collections import defaultdict
from typing import List, Tuple

class Solution:
    def wordsAbbreviation(self, list_of_words: List[str]) -> List[str]:
        def abbreviate(word: str, prefix_length: int) -> str:
            # If abbreviation wouldn't shorten the word meaningfully, return original
            if len(word) - prefix_length <= 2:
                return word
            # abbreviation: prefix + (length- prefix_length -1) + last char
            return word[:prefix_length] + str(len(word) - prefix_length - 1) + word[-1]

        def get_unique_abbreviations(word_index_pairs: List[Tuple[int, str]], prefix_length: int) -> defaultdict:
            abbreviation_map = defaultdict(list)
            for idx, w in word_index_pairs:
                abbreviation = abbreviate(w, prefix_length)
                abbreviation_map[abbreviation].append((idx, w))
            return abbreviation_map

        total_words = len(list_of_words)
        answer_list = [''] * total_words
        word_index_pairs = [(i, w) for i, w in enumerate(list_of_words)]

        abbreviations = get_unique_abbreviations(word_index_pairs, 1)

        for abbr, group in abbreviations.items():
            if len(group) == 1:
                single_index = group[0][0]
                answer_list[single_index] = abbr
            else:
                current_group = list(group)
                current_prefix_length = 2
                while current_group:
                    new_abbreviations = get_unique_abbreviations(current_group, current_prefix_length)
                    current_group = []
                    for new_abbr, new_group_list in new_abbreviations.items():
                        if len(new_group_list) == 1:
                            unique_index = new_group_list[0][0]
                            answer_list[unique_index] = new_abbr
                        else:
                            current_group.extend(new_group_list)
                    current_prefix_length += 1

        return answer_list