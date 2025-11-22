from collections import defaultdict
from typing import List, Tuple

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def abbreviate(word: str, prefix_length: int) -> str:
            if len(word) - prefix_length <= 2:
                return word
            return word[:prefix_length] + str(len(word) - prefix_length - 1) + word[-1]

        def get_unique_abbreviations(words_with_indices: List[Tuple[int, str]], prefix_length: int):
            abbs = defaultdict(list)
            for idx, word in words_with_indices:
                abbs[abbreviate(word, prefix_length)].append((idx, word))
            return abbs

        n = len(words)
        ans = [''] * n
        words_with_indices = list(enumerate(words))

        abbs = get_unique_abbreviations(words_with_indices, 1)

        for abb, group in abbs.items():
            if len(group) == 1:
                idx, word = group[0]
                ans[idx] = abb
            else:
                new_group = list(group)
                prefix_length = 2
                while new_group:
                    new_abbs = get_unique_abbreviations(new_group, prefix_length)
                    new_group = []
                    for new_abb, group_items in new_abbs.items():
                        if len(group_items) == 1:
                            idx, word = group_items[0]
                            ans[idx] = new_abb
                        else:
                            new_group.extend(group_items)
                    prefix_length += 1

        return ans