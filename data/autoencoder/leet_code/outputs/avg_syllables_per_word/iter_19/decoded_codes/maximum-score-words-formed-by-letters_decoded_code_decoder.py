from collections import Counter
from string import ascii_lowercase

class Solution:
    def maxScoreWords(self, words, letters, score):
        def word_score(word, score_map):
            total_score = 0
            for ch in word:
                total_score += score_map[ch]
            return total_score

        def can_form(word, letter_count):
            word_count = Counter(word)
            for ch, cnt in word_count.items():
                if letter_count[ch] < cnt:
                    return False
            return True

        def update_letter_count(letter_count, word, add=True):
            for ch in word:
                if add:
                    letter_count[ch] += 1
                else:
                    letter_count[ch] -= 1

        def backtrack(index, current_score, letter_count):
            if index == len(words):
                return current_score

            max_score = current_score
            for i in range(index, len(words)):
                w = words[i]
                if can_form(w, letter_count):
                    update_letter_count(letter_count, w, add=False)
                    candidate_score = backtrack(i + 1, current_score + word_score(w, score_map), letter_count)
                    if candidate_score > max_score:
                        max_score = candidate_score
                    update_letter_count(letter_count, w, add=True)
            return max_score

        score_map = dict(zip(ascii_lowercase, score))
        letter_count = Counter(letters)

        return backtrack(0, 0, letter_count)