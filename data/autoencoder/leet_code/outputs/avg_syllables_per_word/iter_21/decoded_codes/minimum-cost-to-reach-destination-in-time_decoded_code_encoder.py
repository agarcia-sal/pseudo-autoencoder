import math

class Solution:
    def minCost(self, maxTime, edges, passingFees):
        n = len(passingFees)

        graph = self.create_empty_graph(n)

        for x, y, time in edges:
            self.append_to_graph(graph, x, y, time)

        pq = self.create_priority_queue(passingFees)
        visited_time = self.create_visited_time_list(n)
        visited_time[0] = 0

        while pq:
            current_cost, current_city, current_time = self.pop_from_priority_queue(pq)

            if current_city == n - 1:
                return current_cost

            for neighbor, travel_time in graph[current_city]:
                new_time = current_time + travel_time
                new_cost = current_cost + passingFees[neighbor]

                if new_time <= maxTime and (new_time < visited_time[neighbor] or new_cost < current_cost):
                    visited_time[neighbor] = new_time
                    self.push_to_priority_queue(pq, new_cost, neighbor, new_time)

        return -1

    def create_empty_graph(self, size):
        return [[] for _ in range(size)]

    def append_to_graph(self, graph, x, y, time):
        graph[x].append((y, time))
        graph[y].append((x, time))

    def create_priority_queue(self, passingFees):
        return [(passingFees[0], 0, 0)]

    def create_visited_time_list(self, size):
        return [math.inf] * size

    def pop_from_priority_queue(self, pq):
        pq.sort(key=lambda x: x[0])
        return pq.pop(0)

    def push_to_priority_queue(self, pq, cost, city, time):
        pq.append((cost, city, time))
        pq.sort(key=lambda x: x[0])