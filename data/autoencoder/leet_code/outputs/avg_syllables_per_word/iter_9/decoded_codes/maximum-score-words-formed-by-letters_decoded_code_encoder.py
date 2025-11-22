from collections import Counter

class Solution:
    def maxScoreWords(self, words, letters, score):
        score_map = {chr(i + ord('a')): sc for i, sc in enumerate(score)}
        letter_count = Counter(letters)

        def word_score(word):
            return sum(score_map[ch] for ch in word)

        def can_form(word, letter_count):
            word_count = Counter(word)
            for ch, cnt in word_count.items():
                if letter_count[ch] < cnt:
                    return False
            return True

        def update_letter_count(letter_count, word, add):
            delta = 1 if add else -1
            for ch in word:
                letter_count[ch] += delta

        def backtrack(index, current_score, letter_count):
            if index == len(words):
                return current_score
            max_score = current_score
            for i in range(index, len(words)):
                w = words[i]
                if can_form(w, letter_count):
                    update_letter_count(letter_count, w, False)
                    candidate = backtrack(i + 1, current_score + word_score(w), letter_count)
                    if candidate > max_score:
                        max_score = candidate
                    update_letter_count(letter_count, w, True)
            return max_score

        return backtrack(0, 0, letter_count)