from collections import defaultdict
from typing import List, Dict

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def word_score(word: str, score_map: Dict[str, int]) -> int:
            total_score = 0
            for ch in word:
                total_score += score_map[ch]
            return total_score

        def can_form(word: str, letter_count: Dict[str, int]) -> bool:
            word_count = defaultdict(int)
            for ch in word:
                word_count[ch] += 1
            for ch, cnt in word_count.items():
                if letter_count[ch] < cnt:
                    return False
            return True

        def update_letter_count(letter_count: Dict[str, int], word: str, add: bool) -> None:
            for ch in word:
                if add:
                    letter_count[ch] += 1
                else:
                    letter_count[ch] -= 1

        def backtrack(index: int, current_score: int, letter_count: Dict[str, int]) -> int:
            if index == len(words):
                return current_score

            max_score = current_score
            for i in range(index, len(words)):
                word = words[i]
                if can_form(word, letter_count):
                    update_letter_count(letter_count, word, add=False)
                    candidate_score = backtrack(i + 1, current_score + word_score(word, score_map), letter_count)
                    if candidate_score > max_score:
                        max_score = candidate_score
                    update_letter_count(letter_count, word, add=True)
            return max_score

        score_map = {}
        for i in range(26):
            char = chr(ord('a') + i)
            score_map[char] = score[i]

        letter_count = defaultdict(int)
        for ch in letters:
            letter_count[ch] += 1

        return backtrack(0, 0, letter_count)