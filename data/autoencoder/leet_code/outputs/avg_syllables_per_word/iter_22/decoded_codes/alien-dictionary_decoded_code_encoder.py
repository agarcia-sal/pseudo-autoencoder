from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words):
        graph = defaultdict(set)
        indegree = defaultdict(int)
        all_chars = set(char for word in words for char in word)

        for char in all_chars:
            indegree[char] = 0  # initialize indegree for all characters

        for index in range(len(words) - 1):
            word1 = words[index]
            word2 = words[index + 1]
            min_length = min(len(word1), len(word2))
            found = False

            for position in range(min_length):
                if word1[position] != word2[position]:
                    if word2[position] not in graph[word1[position]]:
                        graph[word1[position]].add(word2[position])
                        indegree[word2[position]] += 1
                    found = True
                    break

            if not found and len(word1) > len(word2):
                return ""

        queue = deque([char for char in all_chars if indegree[char] == 0])
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