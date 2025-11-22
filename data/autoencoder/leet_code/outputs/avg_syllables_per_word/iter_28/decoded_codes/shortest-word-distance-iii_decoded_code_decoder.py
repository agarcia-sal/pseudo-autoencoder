from typing import List
import math

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        min_distance = math.inf
        prev_pos_word1 = -1
        prev_pos_word2 = -1
        words_are_same = (word1 == word2)

        for i, word in enumerate(wordsDict):
            if word == word1:
                if words_are_same:
                    prev_pos_word2 = prev_pos_word1
                prev_pos_word1 = i
            if word == word2 and not words_are_same:
                prev_pos_word2 = i

            if prev_pos_word1 != -1 and prev_pos_word2 != -1:
                dist = abs(prev_pos_word1 - prev_pos_word2)
                if dist < min_distance:
                    min_distance = dist

        return min_distance