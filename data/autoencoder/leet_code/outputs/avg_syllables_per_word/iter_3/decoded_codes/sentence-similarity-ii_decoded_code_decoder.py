class Solution:
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        if len(sentence1) != len(sentence2):
            return False

        parent = {}

        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        for x, y in similarPairs:
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            union(x, y)

        for w1, w2 in zip(sentence1, sentence2):
            parent.setdefault(w1, w1)
            parent.setdefault(w2, w2)
            if find(w1) != find(w2):
                return False

        return True