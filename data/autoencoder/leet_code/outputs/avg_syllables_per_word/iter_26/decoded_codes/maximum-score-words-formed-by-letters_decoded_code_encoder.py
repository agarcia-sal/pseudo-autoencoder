from collections import Counter

class Solution:
    def maxScoreWords(self, words, letters, score):
        def word_score(word, score_map):
            return sum(score_map[ch] for ch in word)

        def can_form(word, letter_count):
            word_count = Counter(word)
            for ch, cnt in word_count.items():
                if letter_count[ch] < cnt:
                    return False
            return True

        def update_letter_count(letter_count, word, add):
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
                word = words[i]
                if can_form(word, letter_count):
                    update_letter_count(letter_count, word, add=False)
                    max_score = max(max_score, backtrack(i + 1, current_score + word_score(word, score_map), letter_count))
                    update_letter_count(letter_count, word, add=True)
            return max_score

        score_map = {chr(ord('a') + i): s for i, s in enumerate(score)}
        letter_count = Counter(letters)

        return backtrack(0, 0, letter_count)