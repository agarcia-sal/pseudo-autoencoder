from collections import Counter
from typing import List

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def word_score(word: str, score_map: dict) -> int:
            total_score = 0
            for ch in word:
                total_score += score_map[ch]
            return total_score

        def can_form(word: str, letter_count: Counter) -> bool:
            word_count = Counter(word)
            for ch, cnt in word_count.items():
                if letter_count[ch] < cnt:
                    return False
            return True

        def update_letter_count(letter_count: Counter, word: str, add: bool) -> None:
            for ch in word:
                if add:
                    letter_count[ch] += 1
                else:
                    letter_count[ch] -= 1

        def backtrack(index: int, current_score: int, letter_count: Counter) -> int:
            if index == len(words):
                return current_score

            max_score = current_score
            for i in range(index, len(words)):
                word = words[i]
                if can_form(word, letter_count):
                    update_letter_count(letter_count, word, False)
                    candidate_score = backtrack(i + 1, current_score + word_score(word, score_map), letter_count)
                    if candidate_score > max_score:
                        max_score = candidate_score
                    update_letter_count(letter_count, word, True)

            return max_score

        score_map = {chr(ord('a') + i): score[i] for i in range(26)}
        letter_count = Counter(letters)

        return backtrack(0, 0, letter_count)