from collections import Counter

class Solution:
    def maxScoreWords(self, words, letters, score):
        def word_score(word, score_map):
            total_score = 0
            for char in word:
                total_score += score_map[char]
            return total_score

        def can_form(word, letter_count):
            word_count = Counter(word)
            for char, count in word_count.items():
                if letter_count[char] < count:
                    return False
            return True

        def update_letter_count(letter_count, word, add):
            for char in word:
                if add:
                    letter_count[char] += 1
                else:
                    letter_count[char] -= 1

        def backtrack(index, current_score, letter_count):
            if index == len(words):
                return current_score

            max_score = current_score
            for i in range(index, len(words)):
                if can_form(words[i], letter_count):
                    update_letter_count(letter_count, words[i], add=False)
                    new_score = backtrack(i + 1, current_score + word_score(words[i], score_map), letter_count)
                    if new_score > max_score:
                        max_score = new_score
                    update_letter_count(letter_count, words[i], add=True)
            return max_score

        score_map = {chr(ord('a') + i): score[i] for i in range(26)}
        letter_count = Counter(letters)
        return backtrack(0, 0, letter_count)