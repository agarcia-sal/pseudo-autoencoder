from typing import List

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        parent = {}

        def find(x: str) -> str:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: str, y: str) -> None:
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        # Initialize parent mapping for all words in similarPairs
        for pair in similarPairs:
            for word in pair:
                if word not in parent:
                    parent[word] = word
        # Union all similar pairs
        for x, y in similarPairs:
            union(x, y)

        # Ensure all words in sentences are in parent
        for x, y in zip(sentence1, sentence2):
            if x not in parent:
                parent[x] = x
            if y not in parent:
                parent[y] = y
            if find(x) != find(y):
                return False

        return True