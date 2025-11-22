from collections import defaultdict

class Solution:
    def wordsAbbreviation(self, words):
        def abbreviate(word, prefix_len):
            if len(word) - prefix_len <= 2:
                return word
            return word[:prefix_len] + str(len(word) - prefix_len - 1) + word[-1]

        def get_unique_abbreviations(words_with_indices, prefix_len):
            abbs = defaultdict(list)
            for idx, word in words_with_indices:
                abbs[abbreviate(word, prefix_len)].append((idx, word))
            return abbs

        n = len(words)
        ans = [""] * n
        words_with_indices = list(enumerate(words))

        abbs = get_unique_abbreviations(words_with_indices, 1)

        for abb, group in abbs.items():
            if len(group) == 1:
                idx, _ = group[0]
                ans[idx] = abb
            else:
                new_group = list(group)
                prefix_len = 2
                while new_group:
                    new_abbs = get_unique_abbreviations(new_group, prefix_len)
                    new_group = []
                    for new_abb, items in new_abbs.items():
                        if len(items) == 1:
                            idx, _ = items[0]
                            ans[idx] = new_abb
                        else:
                            new_group.extend(items)
                    prefix_len += 1

        return ans