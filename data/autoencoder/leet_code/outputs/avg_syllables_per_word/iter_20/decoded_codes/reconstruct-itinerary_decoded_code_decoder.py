from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for dep, dest in sorted(tickets, reverse=True):
            graph[dep].append(dest)

        itinerary = []

        def visit(airport: str):
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]