class Solution:
    def findLUSlength(self, strs):
        def is_subsequence(s, t):
            it = iter(t)
            return all(c in it for c in s)

        strs.sort(key=lambda x: (-len(x), x))
        for i, word in enumerate(strs):
            if all(i == j or not is_subsequence(word, strs[j]) for j in range(len(strs))):
                return len(word)
        return -1