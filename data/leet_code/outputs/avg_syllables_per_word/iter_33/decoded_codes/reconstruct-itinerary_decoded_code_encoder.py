from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)
        itinerary = []

        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]