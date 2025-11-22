from collections import Counter
from string import ascii_lowercase

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        def word_score(word: str, score_map: dict[str, int]) -> int:
            total_score = 0
            for ch in word:
                total_score += score_map[ch]
            return total_score

        def can_form(word: str, letter_count: dict[str, int]) -> bool:
            word_count = Counter(word)
            for ch, cnt in word_count.items():
                if letter_count.get(ch, 0) < cnt:
                    return False
            return True

        def update_letter_count(letter_count: dict[str, int], word: str, add: bool = True) -> None:
            for ch in word:
                if add:
                    letter_count[ch] = letter_count.get(ch, 0) + 1
                else:
                    letter_count[ch] = letter_count.get(ch, 0) - 1

        def backtrack(index: int, current_score: int, letter_count: dict[str, int]) -> int:
            if index == len(words):
                return current_score

            max_score = current_score
            for pos in range(index, len(words)):
                if can_form(words[pos], letter_count):
                    update_letter_count(letter_count, words[pos], add=False)
                    candidate_score = backtrack(pos + 1, current_score + word_score(words[pos], score_map), letter_count)
                    if candidate_score > max_score:
                        max_score = candidate_score
                    update_letter_count(letter_count, words[pos], add=True)
            return max_score

        score_map = {ch: sc for ch, sc in zip(ascii_lowercase, score)}
        letter_count = Counter(letters)

        return backtrack(0, 0, letter_count)