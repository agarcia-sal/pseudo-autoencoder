from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0 or len(words[0]) == 0:
            return []

        word_length = len(words[0])
        num_words = len(words)
        total_length = word_length * num_words
        word_count = Counter(words)
        result = []

        for i in range(len(s) - total_length + 1):
            seen = Counter()
            for j in range(i, i + total_length, word_length):
                word = s[j:j + word_length]
                seen[word] += 1
                if seen[word] > word_count[word]:
                    break
            else:
                result.append(i)

        return result