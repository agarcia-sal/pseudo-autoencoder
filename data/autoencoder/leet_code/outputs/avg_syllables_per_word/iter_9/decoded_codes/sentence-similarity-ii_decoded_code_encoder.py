class Solution:
    def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
        if len(sentence1) != len(sentence2):
            return False

        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        for x, y in similarPairs:
            if x not in parent:
                parent[x] = x
            if y not in parent:
                parent[y] = y

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