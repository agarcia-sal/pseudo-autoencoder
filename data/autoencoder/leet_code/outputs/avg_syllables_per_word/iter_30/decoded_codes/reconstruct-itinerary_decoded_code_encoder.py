from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # Sort tickets and add to graph in reverse order for efficient pop from end
        for frm, to in sorted(tickets, reverse=True):
            graph[frm].append(to)

        itinerary = []

        def visit(airport: str) -> None:
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]