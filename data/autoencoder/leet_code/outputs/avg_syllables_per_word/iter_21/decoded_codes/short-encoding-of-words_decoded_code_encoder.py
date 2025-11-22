class Solution:
    def minimumLengthEncoding(self, words):
        reversed_words = sorted((self.reverse_string(word) for word in words))
        total_length = 0
        for i in range(len(reversed_words)):
            if i == len(reversed_words) - 1 or not reversed_words[i + 1].startswith(reversed_words[i]):
                total_length += len(reversed_words[i]) + 1
        return total_length

    def reverse_string(self, word):
        reversed_word = ''
        for pos in range(len(word) - 1, -1, -1):
            reversed_word += word[pos]
        return reversed_word