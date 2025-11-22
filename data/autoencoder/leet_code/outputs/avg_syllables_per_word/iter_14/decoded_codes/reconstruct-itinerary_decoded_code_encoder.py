from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        # Build the graph with destinations sorted in reverse lex order so we can pop the smallest lex destination last
        for frm, to in sorted(tickets, reverse=True):
            graph[frm].append(to)

        itinerary = []

        def visit(airport: str) -> None:
            while graph[airport]:
                next_dest = graph[airport].pop()
                visit(next_dest)
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]