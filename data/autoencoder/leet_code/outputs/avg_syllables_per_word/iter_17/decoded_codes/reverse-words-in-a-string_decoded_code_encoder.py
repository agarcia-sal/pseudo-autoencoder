class Solution:
    def reverseWords(self, string_s: str) -> str:
        list_of_words = string_s.split()  # splits on any whitespace and removes empty strings
        list_of_words.reverse()
        result_string = ' '.join(list_of_words)
        return result_string