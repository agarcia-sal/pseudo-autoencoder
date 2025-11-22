class Solution:
    def findLongestWord(self, s, dictionary):
        def is_subsequence(word, s):
            it = iter(s)
            for char in word:
                if char not in it:
                    return False
            return True

        dictionary.sort(key=lambda w: (-len(w), w))

        for word in dictionary:
            if is_subsequence(word, s):
                return word
        return ""