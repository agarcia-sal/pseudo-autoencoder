from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for departure, arrival in sorted(tickets, reverse=True):
            graph[departure].append(arrival)

        itinerary = []

        def visit(airport: str) -> None:
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]