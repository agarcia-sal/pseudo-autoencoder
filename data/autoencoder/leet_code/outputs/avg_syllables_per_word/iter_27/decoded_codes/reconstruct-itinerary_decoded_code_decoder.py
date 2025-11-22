from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for dep, arr in sorted(tickets, reverse=True):
            graph[dep].append(arr)

        itinerary = []

        def visit(airport: str) -> None:
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]