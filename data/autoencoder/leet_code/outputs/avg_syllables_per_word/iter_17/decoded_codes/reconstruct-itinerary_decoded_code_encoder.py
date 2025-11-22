from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, list_of_tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # Build graph with destinations sorted in reverse lex order for efficient pop from end
        for source, dest in sorted(list_of_tickets, reverse=True):
            graph[source].append(dest)

        itinerary = []

        def visit(airport: str) -> None:
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]