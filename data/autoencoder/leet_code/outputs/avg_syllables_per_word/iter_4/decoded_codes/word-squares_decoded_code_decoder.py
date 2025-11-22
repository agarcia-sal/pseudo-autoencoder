from collections import defaultdict

class Solution:
    def wordSquares(self, words):
        prefix_to_words = defaultdict(list)
        for word in words:
            for index in range(len(word)):
                prefix = word[:index]
                prefix_to_words[prefix].append(word)

        results = []

        def backtrack(square):
            if len(square) == len(words[0]):
                results.append(square[:])
                return
            prefix = ''
            for word in square:
                prefix += word[len(square)]
            for candidate in prefix_to_words.get(prefix, []):
                backtrack(square + [candidate])

        for word in words:
            backtrack([word])
        return results