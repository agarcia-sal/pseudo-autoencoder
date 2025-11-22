from collections import Counter

class Solution:
    def maxScoreWords(self, words: list[str], letters: list[str], score: list[int]) -> int:
        def word_score(word: str, score_map: dict[str, int]) -> int:
            total_word_score = 0
            for ch in word:
                total_word_score += score_map[ch]
            return total_word_score

        def can_form(word: str, letter_count: Counter) -> bool:
            word_count = Counter(word)
            for ch, cnt in word_count.items():
                if letter_count[ch] < cnt:
                    return False
            return True

        def update_letter_count(letter_count: Counter, word: str, add: bool) -> None:
            if add:
                for ch in word:
                    letter_count[ch] += 1
            else:
                for ch in word:
                    letter_count[ch] -= 1

        def backtrack(index: int, current_score: int, letter_count: Counter) -> int:
            if index == len(words):
                return current_score

            max_score = current_score
            for i in range(index, len(words)):
                if can_form(words[i], letter_count):
                    update_letter_count(letter_count, words[i], add=False)
                    candidate_score = backtrack(i + 1, current_score + word_score(words[i], score_map), letter_count)
                    if candidate_score > max_score:
                        max_score = candidate_score
                    update_letter_count(letter_count, words[i], add=True)
            return max_score

        score_map = {chr(ord('a') + i): score[i] for i in range(26)}
        letter_count = Counter(letters)
        return backtrack(0, 0, letter_count)