class Solution:
    def shortestWordDistance(self, wordsDict: list[str], word1: str, word2: str) -> int:
        min_distance = float('inf')
        prev_word1 = -1
        prev_word2 = -1
        same_word = word1 == word2

        for index, word in enumerate(wordsDict):
            if word == word1:
                if same_word:
                    prev_word2 = prev_word1
                prev_word1 = index
            if word == word2 and not same_word:
                prev_word2 = index
            if prev_word1 != -1 and prev_word2 != -1:
                distance = abs(prev_word1 - prev_word2)
                if distance < min_distance:
                    min_distance = distance

        return min_distance