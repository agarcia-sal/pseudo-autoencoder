from collections import deque

class Solution:
    def shortestPathLength(self, graph):
        if not graph:
            return 0

        number_of_nodes = len(graph)
        queue = self.initialize_queue_with_node_bitmasks(number_of_nodes)
        visited = self.initialize_visited_states_with_node_bitmasks(number_of_nodes)

        steps = 0
        all_nodes_visited = (1 << number_of_nodes) - 1

        while queue:
            for _ in range(len(queue)):
                current_node, visited_nodes = queue.popleft()

                if visited_nodes == all_nodes_visited:
                    return steps

                for neighbor in graph[current_node]:
                    next_visited_nodes = visited_nodes | (1 << neighbor)
                    next_state = (neighbor, next_visited_nodes)
                    if next_state not in visited:
                        visited.add(next_state)
                        queue.append(next_state)
            steps += 1

        return -1

    def initialize_queue_with_node_bitmasks(self, number_of_nodes):
        # Initialize queue with tuples of (node, bitmask) for each node
        return deque((node, 1 << node) for node in range(number_of_nodes))

    def initialize_visited_states_with_node_bitmasks(self, number_of_nodes):
        # Initialize visited set with tuples of (node, bitmask) for each node
        return set((node, 1 << node) for node in range(number_of_nodes))