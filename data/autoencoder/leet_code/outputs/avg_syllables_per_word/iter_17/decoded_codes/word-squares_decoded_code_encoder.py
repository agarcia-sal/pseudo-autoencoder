from collections import defaultdict
from typing import List

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.InitializePrefixToWords(words)
        results = []

        def backtrack(square: List[str]):
            if len(square) == len(words[0]):
                results.append(square[:])
                return

            prefix = self.BuildPrefixFromSquare(square)
            for candidate in self.prefix_to_words.get(prefix, []):
                backtrack(square + [candidate])

        for word in words:
            backtrack([word])

        return results

    def InitializePrefixToWords(self, words: List[str]) -> None:
        self.prefix_to_words = defaultdict(list)
        for word in words:
            for index in range(len(word)):
                prefix = word[:index]
                self.prefix_to_words[prefix].append(word)

    def BuildPrefixFromSquare(self, square: List[str]) -> str:
        prefix = []
        idx = len(square)
        for word in square:
            prefix.append(word[idx])
        return "".join(prefix)