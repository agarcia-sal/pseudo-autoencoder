from collections import defaultdict, deque
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)  # character -> set of characters that come after
        indegree = defaultdict(int)  # character -> number of incoming edges

        all_chars = set(''.join(words))

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
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

        return ''.join(result)