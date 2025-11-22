from collections import Counter
from typing import List, Dict

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        def word_score(word: str, score_map: Dict[str, int]) -> int:
            total_score = 0
            for ch in word:
                total_score += score_map[ch]
            return total_score

        def can_form(word: str, letter_count: Dict[str, int]) -> bool:
            word_count = Counter(word)
            for ch, cnt in word_count.items():
                if letter_count.get(ch, 0) < cnt:
                    return False
            return True

        def update_letter_count(letter_count: Dict[str, int], word: str, add: bool) -> None:
            for ch in word:
                if add:
                    letter_count[ch] = letter_count.get(ch, 0) + 1
                else:
                    letter_count[ch] = letter_count.get(ch, 0) - 1

        def backtrack(index: int, current_score: int, letter_count: Dict[str, int]) -> int:
            if index == len(words):
                return current_score

            max_score = current_score
            for i in range(index, len(words)):
                if can_form(words[i], letter_count):
                    update_letter_count(letter_count, words[i], False)
                    recursive_score = backtrack(
                        i + 1,
                        current_score + word_score(words[i], score_map),
                        letter_count
                    )
                    if recursive_score > max_score:
                        max_score = recursive_score
                    update_letter_count(letter_count, words[i], True)
            return max_score

        # Map 'a' through 'z' to their respective scores
        score_map = {chr(ord('a') + i): score[i] for i in range(26)}
        letter_count = Counter(letters)

        return backtrack(0, 0, letter_count)