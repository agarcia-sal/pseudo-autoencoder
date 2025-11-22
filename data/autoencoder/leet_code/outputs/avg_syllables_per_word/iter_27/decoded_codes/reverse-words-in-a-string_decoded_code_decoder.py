class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        reversed_string = " ".join(words)
        return reversed_string