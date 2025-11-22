class Solution:
    def minimumLengthEncoding(self, list_of_words):
        reversed_words = self.ReverseAndSortWords(list_of_words)
        total_length = 0
        n = len(reversed_words)
        for i in range(n):
            # If it's the last word or the next word does not start with the current word
            if i == n - 1 or not reversed_words[i + 1].startswith(reversed_words[i]):
                # Add length of the current reversed word plus one (for the '#' in encoding)
                total_length += len(reversed_words[i]) + 1
        return total_length

    def ReverseAndSortWords(self, list_of_words):
        # Reverse each word and sort the resulting list
        return sorted(word[::-1] for word in list_of_words)