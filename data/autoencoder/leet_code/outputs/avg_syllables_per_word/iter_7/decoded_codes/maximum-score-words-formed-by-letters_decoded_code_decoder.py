from typing import List
from collections import Counter

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def word_score(word: str, score_map: List[int]) -> int:
            return sum(score_map[ord(c) - ord('a')] for c in word)

        def can_form(word: str, letter_count: Counter) -> bool:
            word_count = Counter(word)
            for c, cnt in word_count.items():
                if letter_count[c] < cnt:
                    return False
            return True

        def update_letter_count(letter_count: Counter, word: str, add: bool) -> None:
            for c in word:
                if add:
                    letter_count[c] += 1
                else:
                    letter_count[c] -= 1

        def backtrack(index: int, current_score: int, letter_count: Counter) -> int:
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

        score_map = score
        letter_count = Counter(letters)
        return backtrack(0, 0, letter_count)