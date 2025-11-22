from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words):
        graph = defaultdict(set)    # char -> set of chars that follow it
        indegree = defaultdict(int) # char -> number of chars before it

        all_chars = set("".join(words))

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_length = min(len(word1), len(word2))
            found = False
            for pos in range(min_length):
                c1, c2 = word1[pos], word2[pos]
                if c1 != c2:
                    if c2 not in graph[c1]:
                        graph[c1].add(c2)
                        indegree[c2] += 1
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