from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        indegree = defaultdict(int)

        all_chars = set(''.join(words))

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            min_length = min(len(word1), len(word2))
            found = False
            for j in range(min_length):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    found = True
                    break
            if not found and len(word1) > len(word2):
                return ""

        queue = deque([c for c in all_chars if indegree[c] == 0])
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