from math import inf

class Solution:
    def shortestWordDistance(self, wordsDict, word1, word2):
        min_distance = inf
        prev_word1 = -1
        prev_word2 = -1
        same_word = word1 == word2

        for index in range(len(wordsDict)):
            word = wordsDict[index]

            if word == word1:
                if same_word:
                    prev_word2 = prev_word1
                prev_word1 = index

            if word == word2:
                if not same_word:
                    prev_word2 = index

            if prev_word1 != -1 and prev_word2 != -1:
                difference = abs(prev_word1 - prev_word2)
                if difference < min_distance:
                    min_distance = difference

        return min_distance