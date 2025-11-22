from collections import defaultdict

class Solution:
    def wordSquares(self, words):
        prefix_to_words = defaultdict(list)
        for word in words:
            for i in range(len(word)):
                prefix = word[:i]
                prefix_to_words[prefix].append(word)

        results = []

        def backtrack(square):
            if len(square) == len(words[0]):
                results.append(square[:])
                return

            prefix = ''.join(word[len(square)] for word in square)
            for candidate in prefix_to_words[prefix]:
                backtrack(square + [candidate])

        for word in words:
            backtrack([word])

        return results