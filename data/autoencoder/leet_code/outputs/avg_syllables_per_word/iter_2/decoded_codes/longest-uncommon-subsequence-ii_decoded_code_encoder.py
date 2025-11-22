class Solution:
    def findLUSlength(self, strs):
        def is_subsequence(s, t):
            it = iter(t)
            for c in s:
                if c not in it:
                    return False
            return True

        strs.sort(key=lambda x: (-len(x), x))

        for i, word in enumerate(strs):
            unique = True
            for j, other in enumerate(strs):
                if i != j and is_subsequence(word, other):
                    unique = False
                    break
            if unique:
                return len(word)

        return -1