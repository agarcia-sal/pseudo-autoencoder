from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words or not words[0]:
            return []

        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_count = Counter(words)
        result = []

        for index in range(len(s) - total_length + 1):
            seen = Counter()
            for position in range(index, index + total_length, word_length):
                word = s[position:position + word_length]
                seen[word] += 1
                if seen[word] > word_count.get(word, 0):
                    break
            else:
                result.append(index)

        return result