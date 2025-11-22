from collections import defaultdict

class Solution:
    def wordsAbbreviation(self, words):
        def abbreviate(word, prefix_length):
            if len(word) - prefix_length <= 2:
                return word
            abbr = word[:prefix_length - 1] + str(len(word) - prefix_length - 1) + word[-1]
            return abbr

        def get_unique_abbreviations(words_with_indices, prefix_length):
            abbs = defaultdict(list)
            for idx, word in words_with_indices:
                abbr = abbreviate(word, prefix_length)
                abbs[abbr].append((idx, word))
            return abbs

        n = len(words)
        ans = [""] * n
        words_with_indices = list(enumerate(words))

        abbs = get_unique_abbreviations(words_with_indices, 1)

        for abbreviation, group in abbs.items():
            if len(group) == 1:
                index, _ = group[0]
                ans[index] = abbreviation
            else:
                new_group = group[:]
                prefix_length = 2
                while new_group:
                    new_abbs = get_unique_abbreviations(new_group, prefix_length)
                    new_group = []
                    for new_abbreviation, new_group_items in new_abbs.items():
                        if len(new_group_items) == 1:
                            index, _ = new_group_items[0]
                            ans[index] = new_abbreviation
                        else:
                            new_group.extend(new_group_items)
                    prefix_length += 1

        return ans