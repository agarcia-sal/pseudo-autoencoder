import heapq
from typing import List, Dict, Tuple

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = self.build_adjacency_list(n, flights)
        min_heap = self.initialize_min_heap(src)
        min_cost = self.initialize_min_cost(src)

        while min_heap:
            cost, stops, city = self.extract_min_element(min_heap)

            if city == dst:
                return cost

            if stops >= k:
                continue

            for neighbor, price in graph[city]:
                next_cost = cost + price
                next_stops = stops + 1

                # Update min_cost and push to heap if this path is better in terms of stops
                if (neighbor not in min_cost) or (next_stops < min_cost[neighbor]):
                    min_cost[neighbor] = next_stops
                    self.push_to_min_heap(min_heap, next_cost, next_stops, neighbor)

        return -1

    def build_adjacency_list(self, n: int, flights: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
        graph = {i: [] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))
        return graph

    def initialize_min_heap(self, src: int) -> List[Tuple[int, int, int]]:
        # heap elements: (cost, stops, city)
        # stops initialized to -1 because the initial city isn't considered a stop yet
        return [(0, -1, src)]

    def initialize_min_cost(self, src: int) -> Dict[int, int]:
        # maps city to minimum stops to reach it; stops start at -1 to align with heap initialization
        return {src: -1}

    def extract_min_element(self, min_heap: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:
        return self.pop_min_from_heap(min_heap)

    def push_to_min_heap(self, min_heap: List[Tuple[int, int, int]], cost: int, stops: int, city: int) -> None:
        self.push_element_to_heap(min_heap, (cost, stops, city))

    def pop_min_from_heap(self, min_heap: List[Tuple[int, int, int]]) -> Tuple[int, int, int]:
        return heapq.heappop(min_heap)

    def push_element_to_heap(self, min_heap: List[Tuple[int, int, int]], element: Tuple[int, int, int]) -> None:
        heapq.heappush(min_heap, element)