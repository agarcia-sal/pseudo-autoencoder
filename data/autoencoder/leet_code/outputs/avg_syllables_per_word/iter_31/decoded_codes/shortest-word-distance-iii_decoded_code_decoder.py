from typing import List
import math

class Solution:
    def shortestWordDistance(self, word_list: List[str], word_one: str, word_two: str) -> int:
        min_distance = math.inf
        prev_word1 = -1
        prev_word2 = -1
        same_word = (word_one == word_two)

        for i, current_word in enumerate(word_list):
            if current_word == word_one:
                if same_word:
                    prev_word2 = prev_word1
                prev_word1 = i
            if current_word == word_two and not same_word:
                prev_word2 = i
            if prev_word1 != -1 and prev_word2 != -1:
                distance = abs(prev_word1 - prev_word2)
                if distance < min_distance:
                    min_distance = distance

        return min_distance