class Solution:
    def reverseWords(self, string_s: str) -> str:
        list_of_words = string_s.split()
        list_of_words.reverse()
        reversed_string = ' '.join(list_of_words)
        return reversed_string