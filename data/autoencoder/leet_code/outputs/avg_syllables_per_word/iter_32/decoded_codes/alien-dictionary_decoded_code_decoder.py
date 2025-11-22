from collections import deque, defaultdict
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)           # character -> set of following characters
        indegree = defaultdict(int)        # character -> number of incoming edges
        all_chars = set(''.join(words))    # all unique characters

        # Initialize indegree for all characters
        for ch in all_chars:
            indegree[ch] = 0

        for index in range(len(words) - 1):
            word1, word2 = words[index], words[index + 1]
            min_length = min(len(word1), len(word2))
            found = False

            for position in range(min_length):
                c1, c2 = word1[position], word2[position]
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
                    found = True
                    break

            # If no difference found and word1 is longer than word2, invalid order
            if not found and len(word1) > len(word2):
                return ""

        queue = deque([ch for ch in all_chars if indegree[ch] == 0])
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