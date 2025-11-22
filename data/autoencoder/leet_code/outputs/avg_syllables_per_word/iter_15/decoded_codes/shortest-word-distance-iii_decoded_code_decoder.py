from math import inf
from typing import List

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_distance = inf
        prev_word1 = -1
        prev_word2 = -1
        same_word = (word1 == word2)

        for i, word in enumerate(wordsDict):
            if word == word1:
                if same_word:
                    prev_word2 = prev_word1
                prev_word1 = i
            if word == word2:
                if not same_word:
                    prev_word2 = i
            if prev_word1 != -1 and prev_word2 != -1:
                min_distance = min(min_distance, abs(prev_word1 - prev_word2))
        return min_distance