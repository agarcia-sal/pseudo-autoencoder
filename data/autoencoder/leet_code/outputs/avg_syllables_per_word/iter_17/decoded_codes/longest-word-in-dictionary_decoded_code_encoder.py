class Solution:
    def longestWord(self, list_of_words):
        list_of_words.sort(key=lambda w: (len(w), w))
        valid_words = set()
        longest_word = ""
        for word in list_of_words:
            if len(word) == 1 or word[:-1] in valid_words:
                valid_words.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word