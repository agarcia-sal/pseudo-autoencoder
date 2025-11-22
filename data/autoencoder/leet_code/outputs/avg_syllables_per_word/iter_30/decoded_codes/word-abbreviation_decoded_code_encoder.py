from collections import defaultdict
from typing import List

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def abbreviate(word: str, prefix_length: int) -> str:
            if len(word) - prefix_length <= 2:
                return word
            return word[:prefix_length] + str(len(word) - prefix_length - 1) + word[-1]

        def get_unique_abbreviations(words_with_indices, prefix_length):
            abbs = defaultdict(list)
            for idx, word in words_with_indices:
                abbs[abbreviate(word, prefix_length)].append((idx, word))
            return abbs

        n = len(words)
        ans = [""] * n
        words_with_indices = list(enumerate(words))
        abbs = get_unique_abbreviations(words_with_indices, 1)

        for abbreviation, group in abbs.items():
            if len(group) == 1:
                idx, _ = group[0]
                ans[idx] = abbreviation
            else:
                new_group = list(group)
                prefix_length = 2
                while new_group:
                    new_abbs = get_unique_abbreviations(new_group, prefix_length)
                    new_group = []
                    for new_abbr, new_group_items in new_abbs.items():
                        if len(new_group_items) == 1:
                            idx, _ = new_group_items[0]
                            ans[idx] = new_abbr
                        else:
                            new_group.extend(new_group_items)
                    prefix_length += 1

        return ans