from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for frm, to in sorted(tickets, reverse=True):
            graph[frm].append(to)

        itinerary = []

        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]