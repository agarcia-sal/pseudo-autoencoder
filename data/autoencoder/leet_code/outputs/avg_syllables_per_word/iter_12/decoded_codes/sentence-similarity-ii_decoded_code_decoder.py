from typing import List, Tuple

class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[Tuple[str, str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        parent = {}

        def find(x: str) -> str:
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x: str, y: str) -> None:
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        # Initialize parents for all words in similarPairs
        for x, y in similarPairs:
            if x not in parent:
                parent[x] = x
            if y not in parent:
                parent[y] = y

        # Union the pairs
        for x, y in similarPairs:
            union(x, y)

        for w1, w2 in zip(sentence1, sentence2):
            if w1 not in parent:
                parent[w1] = w1
            if w2 not in parent:
                parent[w2] = w2
            if find(w1) != find(w2):
                return False

        return True