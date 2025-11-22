class Solution:
    def minimumLengthEncoding(self, words):
        list_of_reversed_words = sorted(word[::-1] for word in words)
        total_length = 0
        n = len(list_of_reversed_words)
        for i in range(n):
            if i == n - 1 or not list_of_reversed_words[i + 1].startswith(list_of_reversed_words[i]):
                total_length += len(list_of_reversed_words[i]) + 1
        return total_length