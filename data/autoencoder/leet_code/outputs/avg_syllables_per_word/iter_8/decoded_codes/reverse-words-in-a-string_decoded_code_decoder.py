class Solution:
    def reverseWords(self, s):
        words = s.split(' ')
        words.reverse()
        result = ' '.join(words)
        return result