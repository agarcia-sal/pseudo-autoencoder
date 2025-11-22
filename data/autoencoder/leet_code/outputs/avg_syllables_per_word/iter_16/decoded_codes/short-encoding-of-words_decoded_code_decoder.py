class Solution:
    def minimumLengthEncoding(self, words):
        reversed_words = sorted(word[::-1] for word in words)
        total_length = 0
        n = len(reversed_words)
        for i in range(n):
            if i + 1 == n or not reversed_words[i+1].startswith(reversed_words[i]):
                total_length += len(reversed_words[i]) + 1
        return total_length