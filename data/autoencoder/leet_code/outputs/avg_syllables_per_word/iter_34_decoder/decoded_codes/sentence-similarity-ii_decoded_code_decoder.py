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
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        for pair in similarPairs:
            for word in pair:
                if word not in parent:
                    parent[word] = word

        for x, y in zip(sentence1, sentence2):
            if x not in parent:
                parent[x] = x
            if y not in parent:
                parent[y] = y
            if find(x) != find(y):
                return False

        for x, y in similarPairs:
            union(x, y)

        return True