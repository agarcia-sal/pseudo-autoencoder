from collections import defaultdict
from typing import List, Dict

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        prefix_to_words: Dict[str, List[str]] = defaultdict(list)

        word_length = len(words[0]) if words else 0

        for word in words:
            for index in range(word_length):
                prefix = word[:index]
                prefix_to_words[prefix].append(word)

        results: List[List[str]] = []

        def backtrack(square: List[str]) -> None:
            current_length = len(square)
            if current_length == word_length:
                results.append(square[:])
                return

            prefix = ''.join(word[current_length] for word in square)

            for candidate_word in prefix_to_words.get(prefix, []):
                backtrack(square + [candidate_word])

        for initial_word in words:
            backtrack([initial_word])

        return results