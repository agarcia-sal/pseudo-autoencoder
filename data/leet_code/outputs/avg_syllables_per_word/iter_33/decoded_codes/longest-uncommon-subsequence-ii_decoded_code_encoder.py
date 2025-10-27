class Solution:
    def findLUSlength(self, strs):
        def is_subsequence(s, t):
            iter_t = iter(t)
            return all(c in iter_t for c in s)

        strs.sort(key=lambda x: (-len(x), x))

        for i, word in enumerate(strs):
            unique = True
            for j, other_word in enumerate(strs):
                if i != j and is_subsequence(word, other_word):
                    unique = False
                    break
            if unique:
                return len(word)
        return -1