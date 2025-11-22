class Solution:
    def minimumLengthEncoding(self, words):
        # Reverse each word and sort them
        reversed_words = sorted(word[::-1] for word in words)
        total_length = 0
        n = len(reversed_words)
        for i in range(n):
            # If last word or next word doesn't start with current word, add its length + 1
            if i == n - 1 or not reversed_words[i + 1].startswith(reversed_words[i]):
                total_length += len(reversed_words[i]) + 1
        return total_length