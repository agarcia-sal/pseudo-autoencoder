from collections import defaultdict
from typing import List

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        prefix_to_words = defaultdict(list)
        for word in words:
            for index in range(len(word)+1):
                prefix = word[:index]
                prefix_to_words[prefix].append(word)

        results = []

        def backtrack(square: List[str]) -> None:
            if len(square) == len(words[0]):
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