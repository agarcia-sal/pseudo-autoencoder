class Solution:
    def shortestWordDistance(self, wordsDict, word1, word2):
        min_distance = float('inf')
        prev_word1 = -1
        prev_word2 = -1
        same_word = (word1 == word2)

        for i in range(len(wordsDict)):
            word = wordsDict[i]
            if word == word1:
                if same_word:
                    prev_word2 = prev_word1
                prev_word1 = i
            if word == word2:
                if not same_word:
                    prev_word2 = i
            if prev_word1 != -1 and prev_word2 != -1:
                dist = abs(prev_word1 - prev_word2)
                if dist < min_distance:
                    min_distance = dist

        return min_distance