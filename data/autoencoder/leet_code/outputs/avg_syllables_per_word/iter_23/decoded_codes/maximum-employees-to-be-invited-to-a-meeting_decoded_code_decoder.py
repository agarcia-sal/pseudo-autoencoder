from collections import defaultdict, deque
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        graph = defaultdict(list)
        in_degree = [0] * n

        # Build the graph and in-degree count
        for i in range(n):
            graph[favorite[i]].append(i)
            in_degree[favorite[i]] += 1

        def find_chain_length(start: int, graph: dict, visited: List[bool]) -> int:
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

        def find_cycle_length(start: int, graph: dict, visited: List[bool], favorite: List[int]) -> int:
            if visited[start]:
                return 0
            stack = []
            current = start
            # Traverse until we find a visited node
            while not visited[current]:
                visited[current] = True
                stack.append(current)
                current = favorite[current]
            if current not in stack:
                return 0
            cycle_start_index = stack.index(current)
            cycle_length = len(stack) - cycle_start_index
            return cycle_length

        mutual_chains = 0
        visited = [False] * n
        # Find all pairs of mutual favorites (two nodes pointing to each other)
        for i in range(n):
            j = favorite[i]
            # Check mutual favorite condition with order to avoid double count
            if favorite[j] == i and i < j:
                # For both nodes, find the max chain length incoming to them excluding each other
                # Use separate visited list per call to prevent interference
                visited_a = [False] * n
                visited_b = [False] * n
                chain_a = find_chain_length(i, graph, visited_a)
                chain_b = find_chain_length(j, graph, visited_b)
                mutual_chains += chain_a + chain_b + 2  # Add 2 for the pair itself

        longest_cycle = 0
        visited = [False] * n
        for i in range(n):
            if not visited[i]:
                cycle_length = find_cycle_length(i, graph, visited, favorite)
                if cycle_length > longest_cycle:
                    longest_cycle = cycle_length

        return max(mutual_chains, longest_cycle)