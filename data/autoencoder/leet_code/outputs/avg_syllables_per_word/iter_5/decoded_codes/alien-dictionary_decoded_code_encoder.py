from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words):
        graph = defaultdict(set)
        indegree = {c: 0 for word in words for c in word}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            found = False
            for j in range(min_len):
                if w1[j] != w2[j]:
                    if w2[j] not in graph[w1[j]]:
                        graph[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    found = True
                    break
            if not found and len(w1) > len(w2):
                return ""

        queue = deque([c for c in indegree if indegree[c] == 0])
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)
            for neigh in graph[char]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    queue.append(neigh)

        if len(result) != len(indegree):
            return ""

        return "".join(result)