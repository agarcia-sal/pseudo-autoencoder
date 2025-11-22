class Solution:
    def wordsAbbreviation(self, words):
        def abbreviate(word, prefix_length):
            if len(word) - prefix_length <= 2:
                return word
            return word[:prefix_length] + str(len(word) - prefix_length - 1) + word[-1]

        def get_unique_abbreviations(words_with_indices, prefix_length):
            abbs = {}
            for index, word in words_with_indices:
                abb = abbreviate(word, prefix_length)
                if abb not in abbs:
                    abbs[abb] = []
                abbs[abb].append((index, word))
            return abbs

        n = len(words)
        ans = [''] * n
        words_with_indices = list(enumerate(words))

        abbs = get_unique_abbreviations(words_with_indices, 1)

        for abb, group in abbs.items():
            if len(group) == 1:
                index, word = group[0]
                ans[index] = abb
            else:
                new_group = []
                for index, word in group:
                    new_group.append((index, word))
                prefix_length = 2
                while len(new_group) > 0:
                    new_abbs = get_unique_abbreviations(new_group, prefix_length)
                    new_group = []
                    for new_abb, new_group_items in new_abbs.items():
                        if len(new_group_items) == 1:
                            index, word = new_group_items[0]
                            ans[index] = new_abb
                        else:
                            new_group.extend(new_group_items)
                    prefix_length += 1

        return ans