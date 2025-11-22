class Solution:
    def findLUSlength(self, list_of_strings):
        def is_subsequence(sequence_s, sequence_t):
            it = iter(sequence_t)
            return all(c in it for c in sequence_s)

        list_of_strings.sort(key=lambda x: (-len(x), x))

        for i, word in enumerate(list_of_strings):
            unique = True
            for j, other in enumerate(list_of_strings):
                if i != j and is_subsequence(word, other):
                    unique = False
                    break
            if unique:
                return len(word)
        return -1