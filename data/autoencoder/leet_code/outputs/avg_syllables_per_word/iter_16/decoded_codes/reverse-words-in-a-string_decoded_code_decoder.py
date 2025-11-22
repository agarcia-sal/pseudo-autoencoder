class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        result_string = ' '.join(words)
        return result_string