from collections import defaultdict
from typing import List, Tuple

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def abbreviate(word: str, prefix_length: int) -> str:
            # If abbreviation wouldn't shorten the word, return original
            if len(word) - prefix_length <= 2:
                return word
            # Construct abbreviation: prefix + count of omitted chars + last char
            return word[:prefix_length] + str(len(word) - prefix_length - 1) + word[-1]

        def get_unique_abbreviations(words_with_indices: List[Tuple[int, str]], prefix_length: int) -> dict:
            abbs = defaultdict(list)
            for idx, w in words_with_indices:
                abbs[abbreviate(w, prefix_length)].append((idx, w))
            return abbs

        n = len(words)
        ans = [''] * n
        words_with_indices = [(i, w) for i, w in enumerate(words)]

        abbs = get_unique_abbreviations(words_with_indices, 1)

        for abb, group in abbs.items():
            if len(group) == 1:
                idx, _ = group[0]
                ans[idx] = abb
            else:
                new_group = group[:]
                prefix_length = 2
                while new_group:
                    new_abbs = get_unique_abbreviations(new_group, prefix_length)
                    new_group = []
                    for new_abb, items in new_abbs.items():
                        if len(items) == 1:
                            idx, _ = items[0]
                            ans[idx] = new_abb
                        else:
                            new_group.extend(items)
                    prefix_length += 1

        return ans