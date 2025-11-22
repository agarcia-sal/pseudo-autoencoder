from collections import defaultdict
from typing import List, Tuple

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def abbreviate(word: str, prefix_length: int) -> str:
            if len(word) - prefix_length <= 2:
                return word
            abbreviated_form = word[:prefix_length]
            number_part = len(word) - prefix_length - 1
            last_character = word[-1]
            return f"{abbreviated_form}{number_part}{last_character}"

        def get_unique_abbreviations(words_with_indices: List[Tuple[int, str]], prefix_length: int) -> dict:
            abbs = defaultdict(list)
            for index, word in words_with_indices:
                abbreviation = abbreviate(word, prefix_length)
                abbs[abbreviation].append((index, word))
            return abbs

        n = len(words)
        ans = [""] * n
        words_with_indices = [(i, word) for i, word in enumerate(words)]

        abbs = get_unique_abbreviations(words_with_indices, 1)

        for abb, group in abbs.items():
            if len(group) == 1:
                index, _ = group[0]
                ans[index] = abb
            else:
                new_group = list(group)
                prefix_length = 2
                while new_group:
                    new_abbs = get_unique_abbreviations(new_group, prefix_length)
                    new_group = []
                    for new_abb, new_group_items in new_abbs.items():
                        if len(new_group_items) == 1:
                            index, _ = new_group_items[0]
                            ans[index] = new_abb
                        else:
                            new_group.extend(new_group_items)
                    prefix_length += 1
        return ans