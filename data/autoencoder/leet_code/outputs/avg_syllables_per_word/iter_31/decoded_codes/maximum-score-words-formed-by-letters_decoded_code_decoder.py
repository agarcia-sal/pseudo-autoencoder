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
            delta = 1 if add else -1
            for ch in word:
                letter_count[ch] += delta

        def backtrack(index, current_score, letter_count):
            if index == len(words):
                return current_score

            max_score = current_score
            for i in range(index, len(words)):
                if can_form(words[i], letter_count):
                    update_letter_count(letter_count, words[i], False)
                    potential_score = backtrack(i + 1, current_score + word_score(words[i], score_map), letter_count)
                    if potential_score > max_score:
                        max_score = potential_score
                    update_letter_count(letter_count, words[i], True)
            return max_score

        score_map = {chr(ord('a') + i): score[i] for i in range(26)}
        letter_count = Counter(letters)
        return backtrack(0, 0, letter_count)