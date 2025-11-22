from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words):
        graph = defaultdict(set)
        indegree = defaultdict(int)

        all_characters = set(''.join(words))
        for c in all_characters:
            indegree[c] = 0

        for i in range(len(words) - 1):
            first_word = words[i]
            second_word = words[i + 1]
            minimum_length = min(len(first_word), len(second_word))
            differing_character_found = False

            for j in range(minimum_length):
                if first_word[j] != second_word[j]:
                    if second_word[j] not in graph[first_word[j]]:
                        graph[first_word[j]].add(second_word[j])
                        indegree[second_word[j]] += 1
                    differing_character_found = True
                    break

            if not differing_character_found and len(first_word) > len(second_word):
                return ""

        queue = deque([c for c in all_characters if indegree[c] == 0])
        result_list = []

        while queue:
            current_character = queue.popleft()
            result_list.append(current_character)
            for neighbor_character in graph[current_character]:
                indegree[neighbor_character] -= 1
                if indegree[neighbor_character] == 0:
                    queue.append(neighbor_character)

        if len(result_list) != len(all_characters):
            return ""

        return ''.join(result_list)