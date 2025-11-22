class Solution:
    def findLUSlength(self, list_of_strings):
        def is_subsequence(string_s, string_t):
            it = iter(string_t)
            return all(c in it for c in string_s)

        list_of_strings.sort(key=lambda x: (-len(x), x))

        for i in range(len(list_of_strings)):
            word = list_of_strings[i]
            unique = True
            for j in range(len(list_of_strings)):
                if i != j and is_subsequence(word, list_of_strings[j]):
                    unique = False
                    break
            if unique:
                return len(word)
        return -1