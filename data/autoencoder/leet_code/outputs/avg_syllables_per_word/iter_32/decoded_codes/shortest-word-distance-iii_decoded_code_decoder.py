from typing import List
import math

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_distance = math.inf
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
                distance_difference = abs(prev_word1 - prev_word2)
                if distance_difference < min_distance:
                    min_distance = distance_difference

        return min_distance