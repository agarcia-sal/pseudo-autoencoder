from collections import defaultdict
from typing import List

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        if not words:
            return []

        # Build prefix hashmap: prefix -> list of words with that prefix
        prefix_to_words = defaultdict(list)
        word_len = len(words[0])

        for word in words:
            for i in range(word_len):
                prefix = word[:i]
                prefix_to_words[prefix].append(word)

        results = []

        def backtrack(square: List[str]) -> None:
            if len(square) == word_len:
                results.append(square[:])
                return

            prefix = ''.join(word[len(square)] for word in square)
            for candidate in prefix_to_words.get(prefix, []):
                backtrack(square + [candidate])

        for word in words:
            backtrack([word])

        return results