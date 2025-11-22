class Solution:
    def longestWord(self, words):
        words.sort(key=lambda w: (len(w), w))  # Sort by length, then lex order
        valid_words = set()
        longest_word = ""
        for word in words:
            if len(word) == 1 or word[:-1] in valid_words:
                valid_words.add(word)
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word