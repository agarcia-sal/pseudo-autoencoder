from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words):
        graph = defaultdict(set)
        indegree = defaultdict(int)
        all_chars = set(ch for word in words for ch in word)

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))
            found = False
            for pos in range(min_length):
                if word1[pos] != word2[pos]:
                    if word2[pos] not in graph[word1[pos]]:
                        graph[word1[pos]].add(word2[pos])
                        indegree[word2[pos]] += 1
                    found = True
                    break
            if not found and len(word1) > len(word2):
                return ""

        queue = deque(ch for ch in all_chars if indegree[ch] == 0)
        result = []

        while queue:
            char = queue.popleft()
            result.append(char)
            for neighbor in graph[char]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(result) != len(all_chars):
            return ""

        return "".join(result)