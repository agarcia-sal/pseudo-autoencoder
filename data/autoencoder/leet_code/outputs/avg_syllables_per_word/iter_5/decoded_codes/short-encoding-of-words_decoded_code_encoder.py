class Solution:
    def minimumLengthEncoding(self, words):
        reversed_words = sorted(word[::-1] for word in words)
        total_length = 0
        for i in range(len(reversed_words)):
            if i == len(reversed_words) - 1 or not reversed_words[i + 1].startswith(reversed_words[i]):
                total_length += len(reversed_words[i]) + 1
        return total_length