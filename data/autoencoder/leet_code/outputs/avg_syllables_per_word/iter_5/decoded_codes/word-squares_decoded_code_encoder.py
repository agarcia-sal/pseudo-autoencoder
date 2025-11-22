from collections import defaultdict

class Solution:
    def wordSquares(self, words):
        n = len(words[0])
        prefix_to_words = defaultdict(list)
        for word in words:
            for i in range(n):
                prefix_to_words[word[:i]].append(word)

        results = []

        def backtrack(square):
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