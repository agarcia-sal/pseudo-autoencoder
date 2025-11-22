from collections import defaultdict
from typing import List, Dict


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n = len(words[0]) if words else 0
        prefix_to_words: Dict[str, List[str]] = defaultdict(list)

        for word in words:
            for i in range(n):
                prefix = word[:i]
                prefix_to_words[prefix].append(word)

        results: List[List[str]] = []

        def backtrack(square: List[str]) -> None:
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