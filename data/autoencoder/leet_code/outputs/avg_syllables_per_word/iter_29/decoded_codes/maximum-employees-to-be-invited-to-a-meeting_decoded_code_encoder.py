from collections import defaultdict, deque

class Solution:
    def maximumInvitations(self, favorite):
        n = len(favorite)
        graph = defaultdict(list)
        in_degree = [0] * n

        for i in range(n):
            graph[favorite[i]].append(i)
            in_degree[favorite[i]] += 1

        def find_chain_length(start, graph, visited):
            length = 0
            queue = deque([start])
            visited[start] = True
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
                        length += 1
            return length

        mutual_chains = 0
        visited = [False] * n
        for i in range(n):
            j = favorite[i]
            if favorite[j] == i and i < j:
                chain_a = find_chain_length(i, graph, visited)
                chain_b = find_chain_length(j, graph, visited)
                mutual_chains += chain_a + chain_b

        def find_cycle_length(start, graph, visited, favorite):
            if visited[start]:
                return 0
            stack = []
            current = start
            while not visited[current]:
                visited[current] = True
                stack.append(current)
                current = favorite[current]
            if current not in stack:
                return 0
            cycle_start_index = stack.index(current)
            return len(stack) - cycle_start_index

        longest_cycle = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                cycle_length = find_cycle_length(i, graph, visited, favorite)
                if cycle_length > longest_cycle:
                    longest_cycle = cycle_length

        return max(mutual_chains, longest_cycle)