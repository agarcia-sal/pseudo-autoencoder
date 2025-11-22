class Solution:
    def shortestWordDistance(self, word_list, first_word, second_word):
        min_distance = float('inf')
        prev_word1 = -1
        prev_word2 = -1
        same_word = first_word == second_word

        for i, word in enumerate(word_list):
            if word == first_word:
                if same_word:
                    prev_word2 = prev_word1
                prev_word1 = i
            if word == second_word:
                if not same_word:
                    prev_word2 = i
            if prev_word1 != -1 and prev_word2 != -1:
                dist = abs(prev_word1 - prev_word2)
                if dist < min_distance:
                    min_distance = dist

        return min_distance