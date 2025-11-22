from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, string_s: str, list_words: List[str]) -> List[int]:
        if not string_s or not list_words or not list_words[0]:
            return []

        word_length = len(list_words[0])
        number_of_words = len(list_words)
        total_length = word_length * number_of_words
        word_count = Counter(list_words)
        result = []

        for index_i in range(len(string_s) - total_length + 1):
            seen = Counter()
            for index_j in range(index_i, index_i + total_length, word_length):
                word = string_s[index_j: index_j + word_length]
                seen[word] += 1
                if seen[word] > word_count[word]:
                    break
            else:
                # Inner loop completed without break
                result.append(index_i)

        return result