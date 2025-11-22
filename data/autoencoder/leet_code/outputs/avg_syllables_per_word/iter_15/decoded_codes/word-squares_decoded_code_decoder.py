from collections import defaultdict
from typing import List

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        prefix_to_words = defaultdict(list)

        for word in words:
            for index in range(len(word)):
                prefix = word[:index]
                prefix_to_words[prefix].append(word)

        results = []
        n = len(words[0]) if words else 0

        def backtrack(square: List[str]):
            if len(square) == n:
                results.append(square)
                return

            prefix_parts = [word[len(square)] for word in square]
            prefix = ''.join(prefix_parts)

            for candidate in prefix_to_words.get(prefix, []):
                backtrack(square + [candidate])

        for word in words:
            backtrack([word])

        return results