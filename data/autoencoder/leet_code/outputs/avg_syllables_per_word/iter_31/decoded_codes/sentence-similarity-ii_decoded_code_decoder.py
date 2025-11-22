from typing import List

class Solution:
    def areSentencesSimilarTwo(
        self,
        sentence1: List[str],
        sentence2: List[str],
        similarPairs: List[List[str]]
    ) -> bool:
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

        for pair in similarPairs:
            for word in pair:
                if word not in parent:
                    parent[word] = word

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