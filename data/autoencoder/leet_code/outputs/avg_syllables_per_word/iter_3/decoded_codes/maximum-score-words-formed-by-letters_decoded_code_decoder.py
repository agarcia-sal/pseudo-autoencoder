from collections import Counter

class Solution:
    def maxScoreWords(self, words, letters, score):
        score_map = {chr(i + ord('a')): val for i, val in enumerate(score)}
        letter_count = Counter(letters)

        def word_score(word):
            return sum(score_map[c] for c in word)

        def can_form(word, letter_count):
            word_count = Counter(word)
            return all(letter_count[c] >= cnt for c, cnt in word_count.items())

        def update_letter_count(letter_count, word, add):
            for c in word:
                letter_count[c] += 1 if add else -1

        def backtrack(index, current_score):
            if index == len(words):
                return current_score

            max_score = current_score
            for i in range(index, len(words)):
                if can_form(words[i], letter_count):
                    update_letter_count(letter_count, words[i], add=False)
                    new_score = backtrack(i + 1, current_score + word_score(words[i]))
                    max_score = max(max_score, new_score)
                    update_letter_count(letter_count, words[i], add=True)
            return max_score

        return backtrack(0, 0)