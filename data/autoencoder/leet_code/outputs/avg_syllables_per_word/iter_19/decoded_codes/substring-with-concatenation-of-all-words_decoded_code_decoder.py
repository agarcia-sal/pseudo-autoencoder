from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        if not s or not words or not words[0]:
            return []

        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_count = Counter(words)
        result = []

        for i in range(len(s) - total_length + 1):
            seen = Counter()
            j = i
            while j < i + total_length:
                word = s[j:j+word_length]
                seen[word] += 1
                if seen[word] > word_count[word]:
                    break
                j += word_length
            else:
                result.append(i)

        return result