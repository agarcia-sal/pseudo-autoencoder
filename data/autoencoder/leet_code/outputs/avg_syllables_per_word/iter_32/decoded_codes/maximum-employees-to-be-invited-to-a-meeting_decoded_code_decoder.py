from collections import defaultdict, deque
from typing import List

class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        graph = defaultdict(list)
        in_degree = [0] * n
        for i in range(n):
            graph[favorite[i]].append(i)
            in_degree[favorite[i]] += 1

        visited = [False] * n
        mutual_chains = 0
        # Find pairs (i, favorite[i]) which are mutual favorites (i.e. favorite[favorite[i]] == i)
        # and i < favorite[i] to avoid double counting
        for i in range(n):
            j = favorite[i]
            if favorite[j] == i and i < j:
                # For each node in the pair, find longest chain leading into it excluding the pair node
                chain_a = self.find_chain_length(i, graph, visited)
                chain_b = self.find_chain_length(j, graph, visited)
                mutual_chains += chain_a + chain_b

        visited = [False] * n
        longest_cycle = 0
        for i in range(n):
            if not visited[i]:
                cycle_length = self.find_cycle_length(i, graph, visited, favorite)
                if cycle_length > longest_cycle:
                    longest_cycle = cycle_length

        return max(mutual_chains, longest_cycle)

    def find_chain_length(self, start: int, graph: defaultdict(list), visited: List[bool]) -> int:
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

    def find_cycle_length(self, start: int, graph: defaultdict(list], visited: List[bool], favorite: List[int]) -> int:
        if visited[start]:
            return 0
        stack = []
        current = start
        # Traverse until we find a visited node
        while not visited[current]:
            visited[current] = True
            stack.append(current)
            current = favorite[current]

        # If current not in stack, no cycle involving start node
        if current not in stack:
            return 0

        cycle_start_index = stack.index(current)
        cycle_length = len(stack) - cycle_start_index
        return cycle_length