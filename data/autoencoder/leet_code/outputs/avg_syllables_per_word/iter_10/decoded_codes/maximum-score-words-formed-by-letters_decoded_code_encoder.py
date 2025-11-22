from collections import Counter

class Solution:
    def maxScoreWords(self, words, letters, score):
        score_map = {chr(ord('a') + i): val for i, val in enumerate(score)}
        letter_count = Counter(letters)

        def word_score(word):
            return sum(score_map[ch] for ch in word)

        def can_form(word):
            word_count = Counter(word)
            for ch, cnt in word_count.items():
                if letter_count[ch] < cnt:
                    return False
            return True

        def update_letter_count(word, add):
            for ch in word:
                letter_count[ch] += 1 if add else -1

        def backtrack(index, current_score):
            if index == len(words):
                return current_score

            max_score = current_score
            for i in range(index, len(words)):
                w = words[i]
                if can_form(w):
                    update_letter_count(w, add=False)
                    candidate_score = backtrack(i + 1, current_score + word_score(w))
                    if candidate_score > max_score:
                        max_score = candidate_score
                    update_letter_count(w, add=True)
            return max_score

        return backtrack(0, 0)