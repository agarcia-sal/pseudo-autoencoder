from collections import defaultdict
from typing import List

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        prefix_to_words = defaultdict(list)
        n = len(words[0]) if words else 0

        # Build prefix dictionary
        for word in words:
            for i in range(n):
                prefix = word[:i]
                prefix_to_words[prefix].append(word)

        results = []

        def backtrack(square: List[str]):
            if len(square) == n:
                results.append(square[:])
                return
            prefix = ''.join(word[len(square)] for word in square)
            for candidate in prefix_to_words.get(prefix, []):
                square.append(candidate)
                backtrack(square)
                square.pop()

        for word in words:
            backtrack([word])

        return results