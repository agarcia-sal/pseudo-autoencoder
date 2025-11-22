class Solution:
    def shortestWordDistance(self, wordsDict, word1, word2):
        min_distance = float('inf')
        prev_word1 = -1
        prev_word2 = -1
        same_word = word1 == word2

        for index, word in enumerate(wordsDict):
            if word == word1:
                if same_word:
                    prev_word2 = prev_word1
                prev_word1 = index
            if word == word2:
                if not same_word:
                    prev_word2 = index
            if prev_word1 != -1 and prev_word2 != -1:
                current_distance = abs(prev_word1 - prev_word2)
                if current_distance < min_distance:
                    min_distance = current_distance
        return min_distance