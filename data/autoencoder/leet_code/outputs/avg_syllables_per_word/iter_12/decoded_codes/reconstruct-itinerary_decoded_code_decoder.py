from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)
        for from_loc, to_loc in sorted(tickets, reverse=True):
            graph[from_loc].append(to_loc)

        itinerary = []

        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)

        visit("JFK")
        return itinerary[::-1]