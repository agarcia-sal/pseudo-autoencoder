from collections import defaultdict
from typing import List

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        prefix_to_words = defaultdict(list)
        length = len(words[0]) if words else 0

        for word in words:
            for index in range(length):
                prefix = word[:index]
                prefix_to_words[prefix].append(word)

        results = []

        def backtrack(square: List[str]) -> None:
            if len(square) == length:
                results.append(square[:])
                return

            prefix = ''.join(word[len(square)] for word in square)
            for candidate in prefix_to_words.get(prefix, []):
                backtrack(square + [candidate])

        for word in words:
            backtrack([word])

        return results