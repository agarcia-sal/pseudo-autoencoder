from collections import defaultdict

class Solution:
    def wordSquares(self, words):
        def initialize_prefix_to_words(words):
            prefix_mapping = defaultdict(list)
            for word in words:
                for i in range(len(word)):
                    prefix = word[:i]
                    prefix_mapping[prefix].append(word)
            return prefix_mapping

        prefix_to_words = initialize_prefix_to_words(words)
        results = []
        n = len(words[0]) if words else 0

        def backtrack(square):
            if len(square) == n:
                results.append(square[:])
                return
            prefix = ''.join(word[len(square)] for word in square)
            for candidate in prefix_to_words.get(prefix, []):
                backtrack(square + [candidate])

        for word in words:
            backtrack([word])

        return results