class Solution:
    def reverseWords(self, s: str) -> str:
        list_of_words = s.split()
        list_of_words.reverse()
        result_string = " ".join(list_of_words)
        return result_string