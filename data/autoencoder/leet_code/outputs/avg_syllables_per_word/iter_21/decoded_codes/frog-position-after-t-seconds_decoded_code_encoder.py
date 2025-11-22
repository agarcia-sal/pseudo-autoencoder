from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n, edges, t, target):
        if n == 1:
            return 1.0

        graph = self.build_graph(edges)
        queue = self.initialize_queue(1, 1.0, 0)
        visited = self.initialize_visited(1)

        while queue:
            current_node, current_probability, current_time = self.dequeue(queue)

            if current_time == t or (current_node != 1 and self.size_of_list(graph[current_node]) == 1):
                if current_node == target:
                    return current_probability
                else:
                    continue

            possible_moves = self.calculate_possible_moves(graph, current_node)

            for neighbor in graph[current_node]:
                if neighbor not in visited:
                    self.add_element(visited, neighbor)
                    self.enqueue(queue, neighbor, current_probability / possible_moves, current_time + 1)

        return 0.0

    def build_graph(self, edges):
        graph = defaultdict(list)
        for edge in edges:
            u, v = edge[0], edge[1]
            graph[u].append(v)
            graph[v].append(u)
        return graph

    def initialize_queue(self, starting_node, current_probability, current_time):
        return deque([(starting_node, current_probability, current_time)])

    def initialize_visited(self, starting_node):
        return {starting_node}

    def size_of_list(self, list_object):
        return len(list_object)

    def calculate_possible_moves(self, graph, current_node):
        if current_node == 1:
            possible_moves = len(graph[current_node])
        else:
            possible_moves = len(graph[current_node]) - 1
        return possible_moves

    def dequeue(self, queue):
        return queue.popleft()

    def enqueue(self, queue, neighbor, probability, time):
        queue.append((neighbor, probability, time))

    def add_element(self, collection, element):
        collection.add(element)