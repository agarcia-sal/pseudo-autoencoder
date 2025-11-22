from collections import defaultdict
from typing import List, Dict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph: Dict[str, List[str]] = defaultdict(list)
        for frm, to in sorted(tickets, reverse=True):
            graph[frm].append(to)

        itinerary: List[str] = []

        def visit(airport: str) -> None:
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]